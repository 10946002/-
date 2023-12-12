import pymysql
import math
connection = pymysql.connect(host='127.0.0.1',
                             user='******',
                             password='******',
                             db='ucard',
                            )

try:
                cursor = connection.cursor()
                delete = "delete FROM ucard.activity;"
                cursor.execute(delete)
                alter = "ALTER TABLE ucard.activity AUTO_INCREMENT = 1"
                cursor.execute(alter)
                connection.commit()
except pymysql.connect.Error as e:
                    print("Error: Could not make connecion to the MySQL database")
                    print(e)

import pandas as pd
df = pd.read_excel("短期資料整理.xlsx",sheet_name="富邦短期")
#print(df)
#print(len(df))#總比數
for i in range(len(df)):
            
            bank=(str(df["銀行別"][i]))
            if len(bank) ==2:
                 bank="0"+bank

            category=str(df["發卡商"][i])
           
            if len(str(df["號碼"][i]))==1:
                id="00"+ str(df["號碼"][i])
            elif len(str(df["號碼"][i]))==2:
                id="0"+ str(df["號碼"][i])
            else :  
                id=str(df["號碼"][i])
            
            '''
            d=int(df["號碼"][i])
            if d<10:
                id="00"+ str(d)
            elif d<100:
                id="0"+ str(d)
            else :  
                id=str(int(d))
             '''
            back=float(df["金額"][i])

            title=str(df["標題"][i])

            start=str(df["開始"][i])

            
            end=str(df["結束"][i])

            condition=float(df["條件"][i])
            if math.isnan(condition ):
                 condition=None

            restriction=float(df["上限"][i])
            if math.isnan(restriction) :
                restriction=None

            store=str(df["店家"][i])


            note=str(df["備註"][i])
            if note=="nan":
                 note=None

            address=str(df["網址"][i])

            state=str(df["狀態"][i])

            #print("cradid",id)
            #print(type(id))

            #print("輸出",id,category,back,bank,title,start,end,condition,limit,store,note,address,state)
    #print("cond型態",type(condition))
    #print("cond值",type(condition))
    #print("lim",type(limit))
    #print("lim輸出",limit)



            try:
                cursor = connection.cursor()
                query = "INSERT INTO activity (bank_id,category,card_id,title,start,end,`feedback`,restriction,`condition`,store,activity_remark,link,state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (bank,category,id,title,start,end,back,restriction,condition,store,note,address,state))
                connection.commit()
                for i in cursor:
                    print(i)
            except pymysql.connect.Error as e:
                    print("Error: Could not make connecion to the MySQL database")
                    print(e)




        
    #print (bank,c,id,name,address)
