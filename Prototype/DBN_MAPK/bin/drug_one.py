import pandas as pd
import pathway_drugged as drugpath
import combination as cmb
import encoder as en


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


df_drug=pd.read_csv("drug.csv",header=None)
df_drug.columns=["Drugs"]
df_drug["Values"]=[0]*7

drugv=list(df_drug["Values"])

cols=["Drug Vector"] + [i for i in range(1,28)]
output_drugone=pd.DataFrame(columns=cols)

j=0

while True:
    encoded=[]
    for i in range(1,28):
        outv=drugpath.pathway([i],drugv,idict)
        encoded.append(float(en.encode(outv)))
    output_drugone.loc[j,"Drug Vector"]=' '.join(map(str,drugv))
    output_drugone.iloc[j,1:]=encoded
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    j=j+1


output_drugone.to_csv("outputDrugOne.csv")

