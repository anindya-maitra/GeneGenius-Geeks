import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
font="serif"

df_cust=pd.read_csv("output_C_pscore.csv",index_col=0)
df_drug=pd.read_csv("output_1_pscore.csv",index_col=0)

df_c=pd.DataFrame(columns=df_cust.columns)
df_d=pd.DataFrame(columns=df_cust.columns)

j=0
li=[]
for i in range(len(df_drug.index)):
    temp=round(df_drug.iloc[i,1],3)
    if temp in li:
        continue
    li.append(temp)
    if temp>25:
        df_d.loc[j]=df_drug.loc[i]
        j+=1

j=0
li=[]
for i in range(len(df_cust.index)):
    temp=round(df_cust.iloc[i,1],3)
    if temp in li:
        continue
    li.append(temp)
    if temp>75:
        df_c.loc[j]=df_cust.loc[i]
        j+=1
        
df_c = df_c.reset_index().drop(["index"], axis=1)
df_d = df_d.reset_index().drop(["index"], axis=1)


plt.figure(figsize=(9,9))
plt.plot(df_d["drug vector"],df_d["condensed weight"],'o-',
         linewidth=1.5,c=(0.8,0,0),label="Known Drugs")
plt.xticks([i for i in range(len(df_c.index)+len(df_d.index))],
            list(df_d["drug vector"])+list(df_c["drug vector"]),
            rotation="vertical",size=9,weight="bold",fontname=font)
plt.yticks(np.arange(0,105,5),size=10,weight="bold",fontname=font)
plt.plot(df_c["drug vector"],df_c["condensed weight"],'o-',
         linewidth=1.5,c=(0,0.5,0),label="Custom Drugs")
plt.xlabel("DRUG VECTOR",fontname=font)
plt.ylabel("EFFICIENCY SCORE",fontname=font)
plt.ylim(20,100)
cl=plt.legend(title="MAPK",loc=4)
plt.setp([cl.texts,cl.get_title()],family=font)
plt.show()
