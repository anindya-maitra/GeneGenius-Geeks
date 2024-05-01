import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

colors=['r','g',]
plt.style.use("fivethirtyeight")
font="serif"


for i in range(1,5):
    plt.figure(figsize=(20,10))
    cols=["drug vector",str(i)+" faults"]
    df1=pd.read_csv("output_"+str(i)+"_pscore.csv",index_col=0)
    df1.columns=cols
    plt.plot(df1.iloc[:,0],df1.iloc[:,1],'.-',c=colors[0],linewidth=1.2,label="GF")
    
    cols=["drug vector",str(i)+" faults"]
    df2=pd.read_csv("C:/Users/arund/Desktop/Final_Year_Project/DBN_MAPK/DBN_MAPK/bin/output_"+str(i)+"_pscore.csv",index_col=0)
    df2.columns=cols
    plt.plot(df2.iloc[:,0],df2.iloc[:,1],'.-',c=colors[1],linewidth=1.2,label="MAPK")
    
    plt.axis("tight")
    plt.xticks([i for i in range(len(df1.index))],df1.iloc[:,0],
            rotation="vertical",size=10,weight="bold",fontname=font)
    plt.yticks(np.arange(0, 100, 5),
           fontname=font,size=10)
    plt.xlabel("DRUG VECTOR",fontname=font)
    plt.ylabel("EFFICIENCY SCORE",fontname=font)
    
    cl=plt.legend(title=str(i)+" fault scenario",loc=4)
    plt.setp(cl.texts,family=font,size=12)
    plt.setp(cl.get_title(),family=font,size=10)
    plt.show()
    