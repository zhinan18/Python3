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
updateUserSize  = "UPDATE test_crop set user_size = %s WHERE corp_id = %s"
try:
    begin = 0
    cursor.execute("SELECT corp_id from test_crop")
    result = cursor.fetchall()
    print("size = ",len(result))
    for corpID in result:
        begin = begin + 1
        cursor.execute("SELECT  user_size from t_department \
        WHERE  `enable` = 1 and corp_id = %s" % corpID)
        corpUserSize = cursor.fetchall()
        if corpUserSize:
            userCount = 0
            for userSize in corpUserSize:
                userCount += userSize[0];
            cursor.execute(updateUserSize, (userCount,corpID))
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

