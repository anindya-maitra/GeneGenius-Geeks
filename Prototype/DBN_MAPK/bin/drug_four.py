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

cols=["Drug Vector"]
for i in range(1,28):
    for j in range(i+1,28):
        for k in range(j+1,28):
            for l in range(k+1,28):
                cols=cols+[str(i)+","+str(j)+","+str(k)+","+str(l)]
output_drugfour=pd.DataFrame(columns=cols)

m=0
while True:
    output_drugfour.loc[m,"Drug Vector"]=' '.join(map(str,drugv))
    n=1
    for i in range(1,28):
        for j in range(i+1,28):
            for k in range(j+1,28):
                for l in range(k+1,28):
                    outv=drugpath.pathway([i,j,k,l],drugv,idict)
                    output_drugfour.iloc[m,n]=en.encode(outv)
                    n=n+1
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    m=m+1


output_drugfour.to_csv("outputDrugFour.csv")


