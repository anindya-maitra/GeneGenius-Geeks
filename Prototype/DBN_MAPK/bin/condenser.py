import pandas as pd

def condense(convert,case=0):
    df_con=pd.DataFrame(columns=["drug vector","condensed weight"])
    df=convert
    base=df.iloc[0,1:]
    max=base.sum()
    len_df=len(df.index)
    for i in range(len_df):
        df_con.loc[i,"drug vector"]=df.iloc[i,0]
        temp=base-df.iloc[i,1:]
        df_con.iloc[i,1]=temp.sum()
    df_con.iloc[:,1]=(df_con.iloc[:,1]/max)*100
    return df_con

