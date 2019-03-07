import itchat,time
from itchat.content import *
import sys
import pymysql
import re
sys.path.append('D:\workspace\python\weixin_account')
from Mysql import Mysql
flag=0
money = 0
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    sql = Mysql()
    now_time = time.strftime("%Y,%m,%d")
    year = now_time.split(",")[0]
    month = now_time.split(",")[1]
    date = now_time.split(",")[2]
    global flag
    global money
    if flag==0:
        if(msg.text=="1" or msg.text=="2" or msg.text=="3"):
            flag=1
        else:
            message = "请输入要进行的操作\n1.记账\n2.显示本月消费\n3.图形化显示每月消费"
    if flag==1:
        if (msg.text == "1"):
            message = "请输入消费金额"
            flag = 2
        elif (msg.text == "2"):
            message = sql.month_consume(month)
        elif (msg.text == "3"):
            message = "模块建设中..."
    elif flag==2:
        money = msg.text
        message = "请选择消费类型\n1.吃饭\n2.水果零食\n3.学习\n4.运动\n0.回到首页"
        flag = 3
    else:
        if(msg.text=="1"):
            message = "吃饭记账成功"
            sql.weixin_account(money,"吃饭",year,month,date)
            print(money)
            flag=0
        elif(msg.text=="2"):
            message = "水果零食记账成功"
            sql.weixin_account(money, "水果零食", year, month, date)
            print(money)
            flag=0
        elif(msg.text=="3"):
            message = "学习用品记账成功"
            sql.weixin_account(money, "学习用品", year, month, date)
            print(money)
            flag=0
        elif(msg.text=="4"):
            message = "运动消费记账成功"
            sql.weixin_account(money, "运动消费", year, month, date)
            print(money)
            flag=0
        else:
            message = "请输入要进行的操作\n1.记账\n2.显示本月消费\n3.图形化显示每月消费"
            flag = 0
    msg.user.send(message)
itchat.auto_login(hotReload=True)
itchat.run(True)