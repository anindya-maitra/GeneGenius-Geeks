import pandas as pd
import pathway_normal as pth
import combination as cmb


df=pd.read_csv("gene.csv", delimiter=",",index_col=0, header=None)
df.columns=["Proteins"]
df["Values"]=[0]*41

inp=df.iloc[:5,:]
out=df.iloc[32:,:]
path=df.iloc[5:32,:]

inpv=list(inp["Values"])
outv=list(out["Values"])
pathv=list(path["Values"])

cols=["Input"] + list(out["Proteins"])
output_fl=pd.DataFrame(columns=cols)

idict={'I1':0,'I2': 0,'I3':0,'I4':0, 'I5':0}


for i in range(32):
    outv=pth.pathway([0],idict)
    output_fl.loc[i,"Input"]=' '.join(map(str,inpv))
    if outv==[0,0,0,0,0,0,0,0,0]:
        unq=list(map(int,(output_fl.loc[i,"Input"]).split(" ")))
    output_fl.iloc[i,1:]=outv
    inpv=cmb.combination(inpv)
    if inpv==False:
        break
    for j in range(5):
        s='I'+str(j+1)
        idict[s]=inpv[j]
    
    
output_fl.to_csv("output_f.csv")

f=open("output_unq.txt","w")
f.write(" ".join(map(str,unq)))
f.close()


    






