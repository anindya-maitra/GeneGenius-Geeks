import pandas as pd
import numpy as np
import combination as cmb
import pathway_drugged as drugpath
from pycuda import driver, compiler, gpuarray, tools
import pycuda.autoinit

import os
if (os.system("cl.exe")):
    os.environ['PATH'] += ';'+r"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\Hostx64\x64"
if (os.system("cl.exe")):
    raise RuntimeError("cl.exe still not found, path probably incorrect")

kernel="""
__global__ void encode(int *outv,float *env)
{
    int tx=threadIdx.x;
    
    int p=tx*(%(outsize)s);
    int f=0,s=0;
    
    for(int i=0;i<%(outsize)s;i++)
    {
        if(i<6)
            f+=outv[p+i];
        else
            s+=outv[p+i];
    }
    env[tx]=0.5*abs(f-s)+0.5*(f*s);
}
"""

#common settings
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
        
#reading protein file
df_gene=pd.read_csv("gene.csv", delimiter=",", index_col=0, header=None)
df_gene.columns=["Proteins"]
df_gene["Values"]=[0] * len(df_gene.index)

#reading drug file
df_drug=pd.read_csv("drug.csv",header=None)
df_drug.columns=["Drugs"]

#pathway and output dataframes
out=pd.DataFrame(df_gene.iloc[32:,:]).reset_index()
path=pd.DataFrame(df_gene.iloc[5:32,:]).reset_index()

#creating output and fault file
faultv=[]
cols=["drug vector"]
for i in range(1,28):
    for j in range(i+1,28):
        for k in range(j+1,28):
            cols=cols+[str(i)+","+str(j)+","+str(k)]
            faultv.append([i,j,k])
output_drugthree=pd.DataFrame(columns=cols)
df_drug=pd.DataFrame(columns=df_drug.iloc[:,0])

#input,pathway,output,encoded matrix for parallelised input
f=open("output_unq.txt","r")
unq=f.readline()
f.close()

inpv=list(map(int,unq.split(" ")))
idict={'I1':0,'I2': 0,'I3':0,'I4':0, 'I5':0}
for j in range(5):
    s='I'+str(j+1)
    idict[s]=inpv[j]

pathv=[0]*len(path)
outv=[[0]*len(out)]* len(faultv)
env=[0] * len(faultv)

#creating drugv file
i=0
drugv=[0]*len(df_drug.columns)
while True:
    df_drug.loc[i]=drugv
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    i=i+1
drugv=(df_drug.to_numpy()).astype(np.int32)

outsize=9
thsize=1024
faultsize=len(faultv)
kernel=kernel % {"outsize":outsize}
mod=compiler.SourceModule(kernel)
results=mod.get_function("encode")
for i in range(len(drugv)):
    for j in range(faultsize):
        outv[j]=drugpath.pathway(faultv[j],drugv[i],idict)
    output_drugthree.loc[i]=" ".join(map(str,drugv[i]))
    thlen=0
    while (thlen+thsize)<faultsize:
        outv_gpu=gpuarray.to_gpu((np.array(outv[thlen:thlen+thsize])).astype(np.int32))
        env_gpu=gpuarray.empty(thsize,np.float32)
        results(outv_gpu,env_gpu,block=(thsize,1,1))
        output_drugthree.iloc[i,thlen+1:thlen+thsize+1]=env_gpu.get()
        thlen=thlen+thsize
    left=faultsize-thlen
    if left>0:
        outv_gpu=gpuarray.to_gpu((np.array(outv[thlen:])).astype(np.int32))
        env_gpu=gpuarray.empty(left,np.float32)
        results(outv_gpu,env_gpu,block=(left,1,1))
        output_drugthree.iloc[i,thlen+1:]=env_gpu.get()


output_drugthree.to_csv("outputDrugThreeP.csv")
