import pymysql as mdb


def mainIn():
    path='orgDeptSort.txt'
    file= open(path,"w",encoding='utf-8')
    sql = "SELECT d.corp_id, d.dept_id FROM t_department d INNER JOIN test1 t on d.corp_id=t.corp_id WHERE `enable`=1 ORDER BY parent_id ASC, priority asc"
    cur.execute(sql)
    rows = cur.fetchall()
    corpId=''"}l"
    deptId=''
    deptNames=''
    j=0
    print("size =", len(rows))
    for row in rows:
        i=0
        for r in row:
            if(i==0):
                corpId=str(r)
            elif(i==1):
                deptId=str(r)
                deptNames=getDeptName(deptId, '')
            i=i+1
        j=j+1
        print(j, corpId+'*'+deptId)
        if(deptNames==''):
            continue
        else:
            file.write(corpId+'$'+deptNames)
            file.write('\n')
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
    con = mdb.connect("localhost", "root", "werered", "test")
    cur = con.cursor()
    mainIn()
    cur.close()
    con.close()