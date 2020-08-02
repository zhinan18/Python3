import pymysql

# 打开数据库连接
localdb = pymysql.connect("localhost", "root", "werered", "test")
webdb = pymysql.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601)
cursor = localdb.cursor()
webCursor = webdb.cursor()
ONE_STEP = 50000
TOTAL = 1200000
userSizeTotal = 0
#sql = "SELECT * FROM user_view_info \
#       WHERE event_id = %s" % (eventId)
insertSQL = "insert into t_department(corp_id, count) value(%s,%d)"
insertDepartment = "insert into corp_user_size(corp_id, user_size) value(%s,%s)"
try:
    for i in range(1, 21):
        cursor.execute("SELECT count(*) from corp_user_size  \
        WHERE user_size = %s" % i)
        corpUserSize = cursor.fetchall()
        userSize=i*int(corpUserSize[0][0])
        print("usre_size = ",i,"共有%s家，共%d人" % (corpUserSize[0][0],userSize))
        userSizeTotal += userSize;
except Exception as e:
        # 发生错误时回滚
    localdb.rollback()
    print(e)
print(userSizeTotal)
localdb.close()
webdb.close()

