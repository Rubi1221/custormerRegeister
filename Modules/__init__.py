#建構Flask物件提供給系統模組來使用(共用)
from flask import Flask
import json
#建構Flask物件
app=Flask('__main__',template_folder='templates',static_folder='wwwroot') #__main__字串視同是一個應用系統名稱 
#Global變數 參照外部config.json 組態檔配置
sysConfig=None
#組態檔config
#with with resource 設定開啟檔案區段 區段結束會自動close
with open('config.json',encoding="UTF-8") as config:
    #使用json模組進行檔案反序列化成物件
    sysConfig=json.load(config)

#引用MVC網站控制器Controller Python模組
import Modules.MemberController
import Modules.MemberService
import Modules.CustomersService