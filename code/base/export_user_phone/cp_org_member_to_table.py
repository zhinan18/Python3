
import pymysql as mdb


def mainIn():
    corpIds = corp_id_tuple()
    try:
        begin = 26077446;
        end = begin + ONE_STEP
        useList = []
        j = 0
        while(end < TOTAL + ONE_STEP):
            webCursor.execute("select * from t_corporation_user \
            WHERE id > '%d' and id <= '%d' and corp_id in %s " % (begin, end, str(corpIds)))
            rows = webCursor.fetchall()
            j += 1
            print('total:',len(rows), j)
            for row in rows:
                if row and len(row) > 0: #corpIDIndex.get(row[1], None):
                    useList.append(row)
            if len(useList) > 0:
                cur.executemany("insert into t_corporation_user (id,corp_id,user_id,name,pinyin,position,authority, \
                email,phone,short_num,fixed_phone,vcode,avatar_original,avatar_thumbnail,created,modified, \
                sync_modified,user_state) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)", useList)
            begin += ONE_STEP
            end += ONE_STEP
            useList.clear()
    except Exception as e:
        con.rollback()
        print(e)


def corp_id_tuple():
    sql = "SELECT corp_id from test1"
    corpID = []
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        if row and row[0]:
            corpID.append(row[0])
    # corpID.append(2372960229)
    return tuple(corpID)



if __name__=='__main__':
    con = mdb.connect("localhost", "root", "werered", "test", charset='utf8')
    # con = mdb.connect(host='127.0.0.1', port=33601, user='wangsheng', passwd='cmcc1234', db="littlec_user",charset='utf8')
    cur = con.cursor()
    webdb = mdb.connect("localhost", "wangsheng", "cmcc1234", "littlec_user", 33601,charset='utf8')
    webCursor = webdb.cursor()
    ONE_STEP = 50000
    # TOTAL = 12
    TOTAL = 30966160

    mainIn()
    cur.close()
    webCursor.close()
    con.commit()
    con.close()
    webdb.close()

