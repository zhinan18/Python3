import pymysql

def copy_admin_info():


    insertSQL = "insert into test_corp(corp_id, province) value(%s,%s)"
    insertGroupSQL = "insert into test2(corp_id) value(%s)"
    insertCrop_adminSQL = "UPDATE test_crop set user_name = %s,phone = %s WHERE user_id = %s"
    try:
        print("begin")
        sql = "SELECT DISTINCT user_id from test_crop WHERE user_id is not NULL and user_id <> 0  and user_size is not NULL and user_size > 0"
        result = corp_id_tuple(sql)
        print("count = ",len(result))
        user_list = []
        ONE_STEP = 5000;
        data_list = []
        count = 0
        for data in result:
            if data:
                data_list.append(data)
                count += 1
                if count == ONE_STEP:
                    count = 0
                    user_list.append(data_list)
                    data_list = []
        if len(data_list) > 0:
            user_list.append(data_list)

        for users in user_list:
            if users and len(users) > 0:
                webCursor.execute("SELECT u.`name`, u.phone,u.user_id from t_user  u WHERE u.user_id in %s " % str(tuple(users)))
                result1 = webCursor.fetchall()
                print("one step user size:" ,len(result1))
                for user in result1:
                    if user and len(user) == 3:
                        cursor.execute(insertCrop_adminSQL, (user[0], user[1], user[2]))

                    # webCursor.execute("SELECT  corp_id, province from t_corporation")
                    # result = webCursor.fetchall()
                    # cursor.executemany(insertSQL, result)

                    # signinCursor.execute("SELECT  corp_id from t_group")
                    # result = signinCursor.fetchall()
                    # cursor.executemany(insertGroupSQL, result)
                    # 执行sql语句
            localdb.commit()

    except Exception as e:
        # 发生错误时回滚
        localdb.rollback()
        print("error db")
        print(e)


def corp_id_tuple(sql):
    if sql:
        ids_list = []
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            if row and row[0]:
                ids_list.append(row[0])
            # corpID.append(1972360106215424)
            # corpID.append(2372960229)
        return tuple(ids_list)

if __name__=='__main__':
    # 打开数据库连接
    localdb = pymysql.connect("localhost", "root", "werered", "test")
    webdb = pymysql.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601)
    cursor = localdb.cursor()
    webCursor = webdb.cursor()

    copy_admin_info()

    localdb.close()
    webdb.close()