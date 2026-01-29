import sys
import pandas as pd

#test sys
print('arguments', sys.argv)

file_name=sys.argv[0]
month=int(sys.argv[1])

print(f"Hello pipeline, month={month}, file={file_name}")

#test pd
df=pd.DataFrame({"day":[1,2],"num_passengers":[3,4]})
df['month']=month
print(df.head())

df.to_parquet(f"output_{month}.parquet")