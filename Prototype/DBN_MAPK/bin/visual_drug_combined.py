import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

colors=['r','b','g','black']
plt.style.use("fivethirtyeight")
font="serif"

plt.figure(figsize=(20,10))
k=0
for i in range(1,5):
    cols=["drug vector",str(i)+" faults"]
    df=pd.read_csv("output_"+str(i)+"_pscore.csv",index_col=0)
    df.columns=cols
    df_sel=pd.DataFrame(columns=cols)
    for j in range(len(df.index)):
        drugv=df.iloc[j,0].split(" ")
        if drugv[3]=='1':
            df_sel.loc[k]=df.loc[j]
            k+=1
    plt.plot(df_sel.iloc[:,0],df_sel.iloc[:,1],'.-',c=colors[i-1],linewidth=1.2,label=str(i)+" fault scenario")
    
plt.axis("tight")
plt.xticks([i for i in range(len(df_sel.index))],df_sel.iloc[:,0],
        rotation="vertical",size=10,weight="bold",fontname=font)
plt.yticks(np.arange(30, 101, 5),
       fontname=font,size=10)
plt.xlabel("DRUG VECTOR",fontname=font)
plt.ylabel("EFFICIENCY SCORE",fontname=font)

cl=plt.legend(title="MAPK")
plt.setp(cl.texts,family=font,size=12)
plt.setp(cl.get_title(),family=font,size=10)
plt.show()
    