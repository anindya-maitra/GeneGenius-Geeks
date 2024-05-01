import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import combination as cmb
import pathway_drugged as drugpath
from pycuda import driver, compiler, gpuarray, tools
import pycuda.autoinit
import os

if (os.system("cl.exe")):
    os.environ['PATH'] += ';'+r"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\Hostx64\x64"
if (os.system("cl.exe")):
    raise RuntimeError("cl.exe still not found, path probably incorrect")
    
#kernel code for parallel encoding
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
plt.style.use("ggplot")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
        
#reading protein file
df_gene=pd.read_csv("gene.csv", delimiter=",", index_col=0, header=None)
df_gene.columns=["Proteins"]
df_gene["Values"]=[0] * len(df_gene.index)

#pathway and output dataframes
out=pd.DataFrame(df_gene.iloc[32:,:]).reset_index()
path=pd.DataFrame(df_gene.iloc[5:32,:]).reset_index()

#input,pathway and output vectors
f=open("output_unq.txt","r")
unq=f.readline()
f.close()

inpv=list(map(int,unq.split(" ")))
idict={'I1':0,'I2': 0,'I3':0,'I4':0, 'I5':0}
for j in range(5):
    s='I'+str(j+1)
    idict[s]=inpv[j]
    
pathv=list(path["Values"])
outv=list(out["Values"])

#reading drug file
df_drug=pd.read_csv("drug.csv",header=None)
df_drug.columns=["Drugs"]

#creating output and fault file
faultv=[]
cols=["Drug Vector"]
col=[]
for i in range(1,28):
    cols=cols+[str(i)]
    faultv.append([i])
output_drugone=pd.DataFrame(columns=cols)

df_drug=pd.DataFrame(columns=df_drug.iloc[:,0])

#input,pathway and output vectors
f=open("output_unq.txt","r")
unq=f.readline()
f.close()

inpv=list(map(int,unq.split(" ")))
idict={'I1':0,'I2': 0,'I3':0,'I4':0, 'I5':0}
for j in range(5):
    s='I'+str(j+1)
    idict[s]=inpv[j]
pathv=[0] * len(path.index)
outv=[[0]*len(out.index)]*len(faultv)

#creating drug file
i=0
drugv=[0,0,0,0,0,0,0]
while True:
    df_drug.loc[i]=drugv
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    i=i+1    

#drugv matrix for parallelised input
drugv=(df_drug.to_numpy()).astype(np.int32)

outsize=9
thlen=len(faultv)
kernel=kernel % {"outsize":outsize}
mod=compiler.SourceModule(kernel)
results=mod.get_function("encode")
for i  in range(len(drugv)):
    for j in range(len(faultv)):
        outv[j]=drugpath.pathway(faultv[j],drugv[i],idict)
    outv_gpu=gpuarray.to_gpu((np.array(outv)).astype(np.int32))
    env_gpu=gpuarray.empty((thlen),np.float32)
    results(outv_gpu,env_gpu,block=(thlen,1,1))
    output_drugone.loc[i]=" ".join(map(str,drugv[i]))
    output_drugone.iloc[i,1:]=env_gpu.get()

output_drugone.to_csv("outputDrugOneP.csv")

      
