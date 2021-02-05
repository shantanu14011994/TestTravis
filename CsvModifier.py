import pandas as pd


 column1="Jurisdiction_Name"
 column2="Jurisdiction_Level"
 column1Values=('FL',)
 df = pd.read_csv("/home/cedcoss/Music/file.csv")
 # print(df)
 # df3 = df[(df.Jurisdiction_Level == "State")]
 # df4 = df3[(df3.Jurisdiction_Name == "FL") | (df3.Jurisdiction_Name == "KS") | (df3.Jurisdiction_Name == "TN")] df4 = df3[(df3.Jurisdiction_Name == "FL") | (df3.Jurisdiction_Name == "KS") | (df3.Jurisdiction_Name == "TN")]
 # df4.to_csv("/home/cedcoss/Music/New.csv")
 # df1=df.query("Jurisdiction_Level==State & Jurisdiction_Name==FL")
 df1=(df.loc[df['Jurisdiction_Name'].isin(['FL','KS','TN','CHANDLER']) & df['Jurisdiction_Level'].isin(['State','City'])])
 df1.to_csv("/home/cedcoss/Music/New.csv")
 # df1=df.query('Jurisdiction_Name=="FL" & Jurisdiction_Name=="KS" Jurisdiction_Name=="TN"')
 # df1.to_csv("/home/cedcoss/Music/file.csv")

def
