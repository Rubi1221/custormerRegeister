#RESTful Service-針對會員資料進行CRUD
from Modules import app #引用Flask物件
from flask import request,make_response #Local Proxy(對應前端個別封裝資訊)
from Modules.DBUtility import createConnection,update
import json
#配合前端瀏覽器維護註冊畫面 採用ajax呼喚進來的服務(註冊使用者資訊)
#前端傳遞一份會員json文件
@app.route("/api/v1/member/add",methods={'POST'})
def memberRegister():
    #透過封裝前端所有資訊的Request物件取出body中所傳遞json
    member=request.get_json() #dict物件
    #會員註冊(呼叫自訂的資料服務模組XxxUtility)
    #取得連接物件(具有開啟連接作用)
    message={} #空的dict物件
    response=make_response()  
    try:
        conn=createConnection()
        #新增作業
        sql='Insert Into Member(UserID,Password,RealName,Email,Role) values(%s,%s,%s,%s,%s)'
        #呼叫資料維護模組update()
        result=update(conn,sql,(member['userName'],member['password'],member['realName'],member['email'],member['role']))
        print(result)
        message={'code':200,'msg':'會員註冊成功!!'}   
          
        response.status=200
        response.content_type="application/json"
        #response.data=message
        #關閉連接
        conn.close()
    except Exception as ex:
        print(ex)
        #回json訊息  
        message={'code':400,'msg':'會員註冊失敗!!'}   
        response.status=400
        response.content_type="application/json"
        

    #設定response header Content-Type
    response.content_type="application/json"
    response.set_data(json.dumps(message)) #序列化物件為json String
    return response   