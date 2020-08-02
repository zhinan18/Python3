import pymysql

# 打开数据库连接
localdb = pymysql.connect("localhost", "root", "werered", "test")
# webdb = pymysql.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601)
cursor = localdb.cursor()
# webCursor = webdb.cursor()
ONE_STEP = 50000
TOTAL = 1200000
#sql = "SELECT * FROM user_view_info \
#       WHERE event_id = %s" % (eventId)
insertSQL = "insert into t_department(corp_id, count) value(%s,%d)"
insertDepartment = "insert into corp_user_size(corp_id, user_size) value(%s,%s)"
try:
    begin = 0
    # end = ONE_STEP
    # while(end < TOTAL):
    # print(begin)
        # webCursor.execute("SELECT  corp_id, user_size from t_department \
        # WHERE id >'%d' and id < '%d'" % (begin, end))
        # result = webCursor.fetchall()
        # cursor.executemany(insertDepartment, result)
    cursor.execute("SELECT corp_id from t_corporation")
    result = cursor.fetchall()
    for corpID in result:
        begin = begin + 1
        cursor.execute("SELECT  corp_id, SUM(user_size) from t_department \
        WHERE corp_id = %s" % corpID)
        corpUserSize = cursor.fetchall()
        if corpUserSize[0][0] != None and corpUserSize[0][1] != None:
            cursor.execute(insertDepartment, corpUserSize[0])
        if begin % 1000 == 0:
            begin = 0
            print("one setp")

    # 执行sql语句
    localdb.commit()
        # print(end)
        # begin += ONE_STEP
        # end   += ONE_STEP
except Exception as e:
        # 发生错误时回滚
    localdb.rollback()
    print(e)

localdb.close()
# webdb.close()

