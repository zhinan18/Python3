import pymysql

# 打开数据库连接
localdb = pymysql.connect("localhost", "root", "werered", "test")
webdb = pymysql.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601)
cursor = localdb.cursor()
webCursor = webdb.cursor()
ONE_STEP = 50000
TOTAL = 30896550
count2017 = 0
count2018 = 0
count2019 = 0
try:
    begin = 0
    end = ONE_STEP
    while(end < TOTAL+ONE_STEP):
        print(begin)
        webCursor.execute("SELECT created from t_user \
        WHERE id >'%d' and id < '%d'" % (begin, end))
        result = webCursor.fetchall()
        for dateT in result:
            if(dateT[0].year <= 2017):
                count2017 = count2017 + 1
            if(dateT[0].year == 2018):
                count2018 = count2018 + 1
            if(dateT[0].year == 2019):
                count2019 = count2019 + 1
        print(end)
        begin += ONE_STEP
        end += ONE_STEP
except Exception as e:
    # 发生错误时回滚
    localdb.rollback()
    print(e)
print("人数情况：", count2017, count2018, count2019)

localdb.close()
webdb.close()

