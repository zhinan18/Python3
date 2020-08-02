import re

import pymysql

# 打开数据库连接
localdb = pymysql.connect("localhost", "root", "werered", "test")
webdb = pymysql.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601)
cursor = localdb.cursor()
webCursor = webdb.cursor()
ONE_STEP = 50000
TOTAL = 25655438
# ONE_STEP = 50
# TOTAL = 550
count2017 = 0
count2018 = 0
count2019 = 0
pat = r"^1(([35789]\d)|(47))\d{8}$"
insertSQL = "insert into user_norealphone(phone,user_id) value(%s,%s)"
try:
    begin = 0
    end = ONE_STEP
    while(end < TOTAL):
        webCursor.execute("SELECT phone,user_id from t_user \
        WHERE id >'%d' and id < '%d'" % (begin, end))
        result = webCursor.fetchall()
        for dateT in result:
            if not re.match(pat, dateT[0]):
                cursor.execute(insertSQL,dateT)
        begin += ONE_STEP
        end += ONE_STEP
        localdb.commit()
        print(end)
except Exception as e:
    # 发生错误时回滚
    localdb.rollback()
    print(e)
localdb.close()
webdb.close()

