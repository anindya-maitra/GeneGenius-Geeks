import pandas as pd
import pathway_custom as drugpath
import encoder as en

#common settings
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
        
#input,pathway and output vectors
f=open("output_unq.txt","r")
unq=f.readline()
f.close()

inpv=list(map(int,unq.split(" ")))
idict={'I1':0,'I2': 0,'I3':0,'I4':0, 'I5':0}
for j in range(5):
    s='I'+str(j+1)
    idict[s]=inpv[j]

#creating custom drug file
df_drug=pd.DataFrame()
df_drug["drug"]=["DRG"+str(i) for i in range(1,28)]

#drugv and encoded lists
drugv=[]
for i in range(27):
    for j in range(i+1,27):
        drugv.append([df_drug.iloc[i,0],df_drug.iloc[j,0]])


#output dataframe
output_custom=pd.DataFrame(columns=["drug"]+[str(i) for i in range(1,28)])

j=0
while True:
    encoded=[]
    for i in range(1,28):
        outv=drugpath.pathway([i],drugv[j],idict)
        encoded.append(en.encode(outv))
    output_custom.loc[j]=[drugv[j][0]+","+drugv[j][1]]+encoded
    inpv=unq[:]
    j=j+1
    if j==len(drugv):
        break
    
#write to csv
output_custom.to_csv("outputDrugCustom.csv")