import pandas as pd
import pathway_normal as pth

df=pd.read_csv("gene.csv", delimiter=",",index_col=0, header=None)
df.columns=["Proteins"]
df["Values"]=[0]*41

out=df.iloc[32:,:]

f=open("output_unq.txt","r")
unq=f.readline()
f.close()

inpv=list(map(int,unq.split(" ")))
idict={'I1':0,'I2': 0,'I3':0,'I4':0, 'I5':0}
for j in range(5):
    s='I'+str(j+1)
    idict[s]=inpv[j]

outv=list(out["Values"])


output1f=pd.DataFrame(columns=["Output Proteins"])
output1f["Output Proteins"]=out["Proteins"]


for i in range(1,28):
    outv=pth.pathway([i],idict)
    output1f[str(i)]=outv

output1f.to_csv("output1f.csv")
