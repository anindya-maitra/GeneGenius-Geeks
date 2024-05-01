import pandas as pd

count_df=pd.read_csv("outv.csv",index_col=0)
count=[0]*len(count_df.index)

k=0
for i in range(4):
    ifile="output"+str(i+1)+"f.csv"
    df=pd.read_csv(ifile,index_col=0)
    count_df["fault" + str(i+1)] = count
    for j in range(len(df.columns)-1):
        out=" ".join(map(str,list(df.iloc[:,j+1])))
        row=list(count_df["output vectors"]).index(out)
        count_df.iloc[row,i+1]=count_df.iloc[row,i+1] + 1
        
count_df.loc[10]=["total"] + [0]*4
for i in range(4):
    count_df.iloc[10,i+1]=count_df.iloc[:,i+1].sum()
    
#write dataframe to file
count_df.to_csv("output_count.csv")