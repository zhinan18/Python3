import pymysql as mdb


def mainIn():
    sql = "SELECT d.dept_id FROM t_department d INNER JOIN test1 t on d.corp_id=t.corp_id WHERE `enable`=1 ORDER BY parent_id ASC, priority DESC"
    insertSql = "insert into depart_sort_name(dept_id, dept_sort_name) value(%s,%s)"
    cur.execute(sql)
    rows = cur.fetchall()
    corpId=''
    deptId=''
    deptNames=''
    j=0
    print("size =", len(rows))
    for row in rows:
        if row and len(row) > 0:
            deptId=str(row[0])
            deptNames=getDeptName(deptId, '')
            print(j, deptId)
        j=j+1
        if(deptNames==''):
            continue
        else:
            cur.execute(insertSql, (deptId, str(deptNames)))
    print('total:',len(rows))
    return 0;


def getDeptName(deptId, deptName):
    sql = "SELECT name,parent_id FROM t_department WHERE dept_id=" + deptId +" AND `enable`=1 limit 1"
    cur.execute(sql)
    rows = cur.fetchall()
    name=''
    parentId=0
    i=0
    for row in rows:
        j=0
        for r in row:
            if(i==0 and j==0):
                name=str(r).replace("\r","").replace("\n","")
            if(i==0 and j==1):
                parentId=r
            j=j+1
        i=i+1
    if(parentId==0):
        deptName=name+'|@|'+deptName
        deptName=deptName[0:len(deptName)-3]
    else:
        tempName = name+'|@|'+deptName
        deptName = getDeptName(str(parentId),tempName)
    return deptName
if __name__=='__main__':
    # con = mdb.connect(host='127.0.0.1', port=33601, user='wangsheng', passwd='cmcc1234', db="littlec_user", charset='utf8')
    con = mdb.connect("localhost", "root", "werered", "test",charset='utf8')
    cur = con.cursor()
    mainIn()
    con.commit()
    cur.close()
    con.close()