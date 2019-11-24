import pymysql

# 打开数据库连接
localdb = pymysql.connect("localhost", "root", "werered", "test")
webdb = pymysql.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601)
cursor = localdb.cursor()
webCursor = webdb.cursor()
ONE_STEP = 500000
TOTAL = 30896550
#sql = "SELECT * FROM user_view_info \
#       WHERE event_id = %s" % (eventId)
insertSQL = "insert into user_phone(corp_id, phone) value(%s,%s)"
try:
    begin = 0
    end = ONE_STEP
    while(end < TOTAL):
        print(begin)
        webCursor.execute("SELECT  u.corp_id, u.phone from t_corporation_user u  INNER JOIN t_corporation c ON u.corp_id=c.corp_id \
        WHERE u.id >'%d' and u.id < '%d' and c.province=50" % (begin, end))
        result = webCursor.fetchall()
        cursor.executemany(insertSQL, result)
        # 执行sql语句
        localdb.commit()
        print(end)
        begin += ONE_STEP
        end   += ONE_STEP
except:
    # 发生错误时回滚
    localdb.rollback()
    print("error db")

localdb.close()
webdb.close()

