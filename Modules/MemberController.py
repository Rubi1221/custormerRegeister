#引用Flask物件 定義端點
#針對會員Member CRUD(Create/Read/Update/Delete)
from Modules import app,sysConfig
#request variable一個一個對應前端的請求
from flask import render_template,request

#定義一個端點 進行會員註冊作業(採用調用頁面)
#限制請求 具有方法 request Method=GET(使用超連結)
@app.route('/member/register/form',methods=['GET'])
def register():
    #取出角色項目與說明
    roleList=sysConfig['roles']
    descrList=sysConfig['rolesDescr']
    print(roleList)
    #使用樣板引擎調用頁面 持續角色list狀態 到頁面去進行後端Expression(Render)
    return render_template("memberegister.html",roles=roleList,descrs=descrList)
    