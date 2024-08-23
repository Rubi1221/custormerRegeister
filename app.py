#應用系統Startup 啟動點 需要Flask物件
from Modules import app
from flask import render_template


#配置首頁(這一個py 就是Controller)
#home action(函數)
#描述端點
@app.route('/') #route method 是Python Decorator(語法糖架構)
@app.route('/home')
def home():
    #調用一個首頁View Page,經由jinja2 引擎  借住一個render_tremplate function
    #帶入一個參數(網頁)給樣板引擎 進行Expression...->再產生標準的HTML String進行回應使用者端
    dispatcher=render_template("index.html")
    print(dispatcher)
    return dispatcher

#主程式
if __name__=='__main__':
    #啟動網站系統
                                           
    app.run(host='localhost',port=8899)