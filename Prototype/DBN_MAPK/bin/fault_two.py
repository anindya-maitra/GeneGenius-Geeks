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


output2f=pd.DataFrame(columns=["Output Proteins"])
output2f["Output Proteins"]=out["Proteins"]

for i in range(1,28):
    for j in range(i+1,28):
        s=str(i)+","+str(j)
        outv=pth.pathway([i,j],idict)
        output2f[s]=outv
    

output2f.to_csv("output2f.csv")
