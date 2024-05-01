import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import condenser as cond

plt.style.use("fivethirtyeight")
font="serif"

df_drugcustom=pd.read_csv("outputDrugCustom.csv",index_col=0)

col_df=len(df_drugcustom.columns[1:])
len_df=len(df_drugcustom.index)

#calculate Probabilistic Score
df_con=cond.condense(df_drugcustom)
df_con.to_csv("output_C_pscore.csv")
df_con=pd.read_csv("output_C_pscore.csv",index_col=0)

#scatter: drug vector v probabilistic score
plt.figure(figsize=(64,32))
plt.plot([i for i in range(len_df)],df_con.iloc[:,1],".-",c="r",linewidth=1.2)
plt.axis("tight")
plt.xticks([i for i in range(len_df)],df_con.iloc[:,0],rotation="vertical",
           size=10,weight="bold",fontname=font)
plt.yticks(np.arange(min(df_con.iloc[:,1]), max(df_con.iloc[:,1])+5, 5))
plt.xlabel("DRUG VECTOR",fontname=font)
plt.ylabel("PROBABILISTIC SCORE",fontname=font)
plt.show()
