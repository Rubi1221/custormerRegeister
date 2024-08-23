#提供端點進行客戶CRUD
from Modules import app #引用Flask物件
from flask import render_template,make_response,request
from Modules.DBUtility import query,update,createConnection
import json
#----------------------------MVC Web網站--------------------------------------
#調用客戶查詢頁面
@app.route('/customers/qry/bycountry',methods=['GET'])
def customersQry():
    #調用頁面 交給Jinja2引擎調用頁面
    return render_template('customersqrycountry.html')

#--------------------------RESTful Service軟體風格-------------------------------------
#前端傳遞國家別 找出相對國家別客戶資料 查詢 request methods - get
@app.route("/api/v1/customers/qry/<country>/rawdata",methods=['GET'])
def customersCountry(country):
    #呼叫模組進行查詢
    #建構一個Response物件
    response=make_response()
    response.content_type="application/json"
    #取得連接物件
    try:
        conn=createConnection('NORTHWND') #具有開啟連接上資料庫
        sql="select CustomerID,CompanyName,Address,Phone,Country from Customers Where Country=%s"
        #呼叫查詢模組
        result=query(conn,sql,(country),True)
        if len(result)==0:
                #查無資料
                msg={'code':400,'message':f'查無國家別:{country} 的客戶資料'}
                response.status_code=400
                response.set_data(json.dumps(msg))
        else:    
            #空list物件
            resultList=[]
            #整理tupe為dict(具有屬性名稱) 逐筆走訪
            for index in range(len(result)):
                #參考出tupe
                rec=result[index]
                #建構dict
                recDict={'customerId':rec[0],'companyName':rec[1],'address':rec[2],'phone':rec[3],'country':rec[4]}
                resultList.append(recDict)

            response.status_code=200
            response.set_data(json.dumps(resultList))    

    except Exception as ex:
        #後端有問題
        msg={'code':500,'message':f'後端有問題，請聯絡管理員'}
        response.status_code=500
        response.set_data(json.dumps(msg))

    return response 

#進行客戶刪除作業服務 Request Method-DELETE
#採用QueryString傳遞客戶編號 cid=xxxx
@app.route('/api/v1/customers/delete',methods=['DELETE'])
def customersDelete():
    #使用底層request local proxy 進行參數取得
    customerid=request.args.get('cid')
    #sql
    sql='DELETE FROM Customers Where CustomerID=%s'
    message={}
    #產生回應的Response物件
    response=make_response()
    response.content_type="application/json"
    try:
        #跟模組要一條連接物件 連接上northwnd
        conn=createConnection('NORTHWND')
        #先進行查詢(看看是否存在這一筆資料) 查詢語法統計紀錄數 有回1 沒有0
        rawdata=query(conn,'select count(*) as counter from Customers where CustomerID=%s',(customerid))
        print(rawdata) #tuple(,)取第一個值
        if rawdata[0]==1:
            #呼叫update function
            update(conn,sql,(customerid))
            message={'code':200,'message':f'客戶資料:{customerid} 刪除成功'}
            response.status_code=200
            response.set_data(json.dumps(message))
        else:
           message={'code':400,'message':f'客戶資料:{customerid} 不存在'}
           response.status_code=400
           response.set_data(json.dumps(message))     

        
    except Exception as ex:
        message={'code':400,'message':f'客戶資料:{customerid} 刪除失敗'}
        response.status_code=400  
        response.set_data(json.dumps(message))

    return response   