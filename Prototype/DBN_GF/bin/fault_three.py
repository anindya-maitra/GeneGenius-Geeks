import pandas as pd
import pathway_normal as pth

df=pd.read_csv("gene.csv", delimiter=",",index_col=0, header=None)
df.columns=["Proteins"]
df["Values"]=[0]*36

out=df.iloc[29:,:]

f=open("output_unq.txt","r")
unq=f.readline()
f.close()

inpv=list(map(int,unq.split(" ")))
idict={'I1':0,'I2': 0,'I3':0,'I4':0, 'I5':0}
for j in range(5):
    s='I'+str(j+1)
    idict[s]=inpv[j]

outv=list(out["Values"])


output3f=pd.DataFrame(columns=["Output Proteins"])
output3f["Output Proteins"]=out["Proteins"]


for i in range(1,25):
    for j in range(i+1,25):
        for k in range(j+1,25):
            s=str(i)+","+str(j)+","+str(k)
            outv=pth.pathway([i,j,k],idict)
            output3f[s]=outv
    

output3f.to_csv("output3f.csv")
