import pandas as pd
import requests
import xlwings as xw
import time

url="https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
headers={
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    
}
session=requests.Session()
data=session.get(url, headers=headers).json()["records"]["data"]
ocdata=[]
for i in data:
    for j,k in i.items():
        if j=="CE" or j=="PE":
         info=k
         info["instrumentType"]=j
         ocdata.append(info)
        
df=pd.DataFrame(ocdata)
wb=xw.Book("Data.xlsx")
st=wb.sheets("nifty.2")
st.range("A1").value = df
time.sleep(30)       
