import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = sns.load_dataset("titanic")
pd.set_option("display.max_columns",None)
df=data.copy()
df.head()
df.info()

# all categorical values selected from df
cat_cols=[col for col in df.columns
          if str(df[col].dtype)
          in ["bool","category","object"]]
# Numerical but actually categorical values from df
num_but_cat = [col for col in df.columns
               if df[col].nunique()<10
               and df[col].dtypes
               in ["int64","float64"]]
# categorical but actually cardinal values from data
cat_but_car=[col for col in df.columns if df[col].nunique() >20 and str(df[col].dtypes) in ["cateorical","object"]]

# all categorical datas selected
cat_cols = num_but_cat + cat_cols
cat_cols = [col for col in cat_cols if col not in cat_but_car ]

#finding and plotting categorical values
def plotting(df,col_name,plot=False):

    if df[col_name].dtypes =="bool":
        df[col_name]=df[col_name].astype(int)

        print(pd.DataFrame({col_name: df[col_name].value_counts(),
                            "Percentage":100 * df[col_name].value_counts() / len(df)}))
        if plot:
            sns.countplot(x=df[col_name], data=df)
            plt.show(block=True)

    else:
        print(pd.DataFrame({col_name: df[col_name].value_counts(),
                            "Percentage":100 * df[col_name].value_counts() / len(df)}))
        if plot:
            sns.countplot(x=df[col_name], data=df)
            plt.show(block=True)

#finding and plotting numerical values
def numerical(df,col_name,plot=False):
    if df[col_name].dtypes in ["int64","float64"] and df[col_name].nunique()>5:
        print(df[col_name].describe().T)

        if plot:
            sns.histplot(data=df,x=df[col_name])
            plt.xlabel(col_name)
            plt.title(col_name)
            plt.show(block=True)
    else:
        print("your value is categorical, not numerical")

numerical(df,"age",plot=True)
