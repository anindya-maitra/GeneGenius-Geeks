import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import condenser as cond

plt.style.use("fivethirtyeight")
font="serif"

df_drugfour=pd.read_csv("outputDrugFourP.csv",index_col=0)

col_df=len(df_drugfour.columns[1:])
len_df=len(df_drugfour.index)

#calculate Probabilistic Score
df_con=cond.condense(df_drugfour)
df_con.to_csv("output_4_pscore.csv")
df_con=pd.read_csv("output_4_pscore.csv",index_col=0)

#scatter: drug vector v probabilistic score
plt.figure(figsize=(20,10))
plt.plot([i for i in range(len_df)],df_con.iloc[:,1],".-",c="r",linewidth=1.2)
plt.axis("tight")
plt.xticks([i for i in range(len_df)],df_con.iloc[:,0],rotation="vertical",
           size=10,weight="bold",fontname=font)
plt.yticks(np.arange(0, 100, 5), fontname=font,size=10,weight="bold")
plt.xlabel("DRUG VECTOR",fontname=font)
plt.ylabel("PROBABILISTIC SCORE",fontname=font)
plt.show()