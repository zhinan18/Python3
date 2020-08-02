import pymysql

# 打开数据库连接
localdb = pymysql.connect("localhost", "root", "werered", "test")
webdb = pymysql.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601)
cursor = localdb.cursor()
webCursor = webdb.cursor()
ONE_STEP = 1000
TOTAL = 23699000
#sql = "SELECT * FROM user_view_info \
#       WHERE event_id = %s" % (eventId)
insertSQL = "insert into user_phone(corp_id, phone, authority) value(%s,%s,%s)"
try:
    begin = 25662244
    end = begin + ONE_STEP
    while(end <= TOTAL+ ONE_STEP):
        print(begin)
        webCursor.execute("SELECT  u.corp_id, u.phone, u.authority from t_corporation_user u \
        WHERE u.id >'%d' and u.id < '%d' and u.authority > 1" % (begin, end))
        result = webCursor.fetchall()
        cursor.executemany(insertSQL, result)
        # 执行sql语句
        localdb.commit()
        print(end)
        begin += ONE_STEP
        end   += ONE_STEP
except Exception as e:
    # 发生错误时回滚
    localdb.rollback()
    print("error db")
    print(e)

localdb.close()
webdb.close()

