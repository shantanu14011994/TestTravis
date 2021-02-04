import pandas as pd


def filter(filepath,columndict,sortdict):
    df=pd.read_csv(filepath)
    for col,col_val in columndict.items():
        df1= (df.loc[df[col].isin(list(col_val.split("-")))])
    # for colsort,orderbool in sortdict.items():
    df2=df1.sort_values(list(sortdict.keys()),ascending=list(sortdict.values()))
    df2.to_csv(filepath)


    """
  
    filter(filepath,columndictionary,sortingcolumndictionary)
    
    :parameter
    
    filepath: Here you will give the path to your csv
    
    columndictionary: Here you will give Column Name as keys and Column Values as values
    python dictionaries has keys and values like {"keys":"values"}
    for multiple column values of a column, dictionary looks like-{"column1":"value1-value2-value3-..."}
    
    sortingcolumndictionary:Here you will give column,which you want to sort, as keys.
    If you want your column to be in ascending order,give value of that column as True, otherwise False
    
    
    
    """

filter("/home/cedcoss/Music/file.csv",{"Jurisdiction_Level":"State","Jurisdiction_Name":"FL-KS-TN"},
        {"Jurisdiction_Name":True,"Order_ID":True,"Financial_Component":True,"Transaction_Type":False}
       )



