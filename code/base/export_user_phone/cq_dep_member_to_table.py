
import pymysql as mdb


def mainIn():
    # 获取企业ID的索引
    # corpIDIndex = corp_id()
    insertDeptUser = ""
    corpIDs = corp_id_tuple()
    print(str(corpIDs))
    try:
        begin = 0;
        end = ONE_STEP
        useList = []
        j = 0
        while(end < TOTAL + ONE_STEP):
            webCursor.execute("select * from t_department_user \
            WHERE id > '%d' and id <= '%d' and corp_id in %s " % (begin, end,str(corpIDs)))
            rows = webCursor.fetchall()
            j += 1
            print('total:', len(rows), j)
            for row in rows:
                if row and len(row) > 0: #corpIDIndex.get(row[1], None):
                    useList.append(row)
            if len(useList) > 0:
                cur.executemany("insert into t_department_user (id, corp_id, dept_id, user_id, duty, order_rule, \
                                created, modified, sync_modified, enable) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)", useList)
            begin += ONE_STEP
            end += ONE_STEP
            useList.clear()
    except Exception as e:
        con.rollback()
        print(e)


def corp_id():
    sql = "SELECT corp_id from test1"
    corpID = {}
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        if row and len(row) > 0:
            corpID[row[0]] = row[0]
    print( len(corpID))
    # corpID[2372960229] =2372960229
    return corpID

def corp_id_tuple():
    sql = "SELECT corp_id from test1"
    corpID = []
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        if row and row[0]:
            corpID.append(row[0])
    # corpID.append(1972360106215424)
    # corpID.append(2372960229)
    return tuple(corpID)



if __name__=='__main__':
    con = mdb.connect("localhost", "root", "werered", "test", charset='utf8')
    # con = mdb.connect(host='127.0.0.1', port=33601, user='wangsheng', passwd='cmcc1234', db="littlec_user",charset='utf8')
    cur = con.cursor()
    webdb = mdb.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601)
    webCursor = webdb.cursor()
    ONE_STEP = 50000
    TOTAL = 26077446

    mainIn()
    cur.close()
    webCursor.close()
    con.commit()
    con.close()
    webdb.close()

