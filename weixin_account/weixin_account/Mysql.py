import pymysql

class Mysql(object):
    def __init__(self):
        self.db = pymysql.connect('localhost','root','root','weixin_account')
        self.cursor = self.db.cursor()
    def weixin_account(self,money,consume_type,year,month,date):
        sql = "insert into weixin_consume(money,consume_type,year,month,date) values("+money+",'"+consume_type+"',"+year+","+month+","+date+");"

        self.cursor.execute(sql)
        self.db.commit()
    def month_consume(self,month):
        sql = "select consume_type,money from weixin_consume where month = "+month
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        consume = {}
        consume['吃饭']=""
        consume['水果零食']=""
        consume['运动消费']=""
        consume['学习用品']=""
        for r in results:
            consume[r[0]] = str(r[1])+"+"+consume[r[0]]
        message = ''
        for c in consume.keys():
            S = consume[c].split("+")
            sum = 0
            for s in S:
                if(s != ''):
                    sum = sum + int(s)
            message = message + c + ":"+consume[c]+" = "+str(sum)+"\n"
        return message