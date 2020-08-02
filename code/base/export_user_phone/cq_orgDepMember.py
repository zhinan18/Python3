import pymysql as mdb
import time

# 测试函数运行时间
def cal_time(fn):
    """计算性能的修饰器"""
    def wrapper(*args,**kwargs):
        starTime = time.time()
        f = fn(*args,**kwargs)
        endTime = time.time()
        print('%s() runtime:%s ms' % (fn.__name__, 1000*(endTime - starTime)))
        return f
    return wrapper

fileName = "orgDepMember.txt"

@cal_time
def mainIn(begin, step):
    file= open(fileName, "a+", encoding='utf-8')
    sql = "SELECT corp_id, user_id, dept_id, duty,order_rule FROM t_department_user WHERE `enable` = 1  limit " +str(begin)+ ","+ str(step)
    cur.execute(sql)
    rows = cur.fetchall()
    print('total:', len(rows))
    corpId=''
    userId =''
    deptId=''
    deptName=''
    phone=''
    duty=''
    type='0'
    orderRule='0'
    j=0
    for row in rows:
        i=0
        for r in row:
            if(i==0):
                corpId=str(r)
            if(i==1):
                userId=str(r)
                phone=getPhone(userId)
            elif(i==2):
                deptId=str(r)
                deptName = getDeptName(deptId)
                type = getType(deptId, corpId, userId)
            elif(i==3):
                duty=str(r).replace("\r","").replace("\n","").replace("$","-")
            elif(i==4):
                orderRule=str(r)
            i=i+1
        if(phone!='' and deptName != ''):
            file.write(corpId+'$'+deptName +'$'+phone+'$'+duty+'$'+type+'$'+orderRule)
            file.write('\n')
        j = j + 1
        print(j, corpId, userId, phone, type, orderRule)
    return 0;


def getType(deptId, corpId,userId):
    sql = "SELECT corp_id FROM t_corporation_admin WHERE corp_id="+corpId+" and user_id="+userId+" and dept_id="+deptId+" AND `enable`=1   LIMIT 1"
    cur.execute(sql)
    rows = cur.fetchall()
    if(len(rows)==1):
        return '1'
    return '0';

def getDeptName(deptId):
    sql = "SELECT dept_sort_name from depart_sort_name WHERE dept_id =" + deptId + " limit 1"
    cur.execute(sql)
    rows = cur.fetchall()
    if rows and len(rows) > 0:
        return str(rows[0][0])
    else:
        return ""

def getPhone(userId):
    sql = "SELECT phone FROM t_corporation_user WHERE user_id=" + userId + " limit 1"
    cur.execute(sql)
    rows = cur.fetchall()
    if(len(rows)==0):
        return ''
    else:
        return str(rows[0][0])

if __name__=='__main__':
    con = mdb.connect("localhost", "root", "werered", "test", charset='utf8')
    # con = mdb.connect(host='127.0.0.1', port=33601, user='wangsheng', passwd='cmcc1234', db="littlec_user",charset='utf8')
    cur = con.cursor()
    sql = "SELECT count(*) FROM t_department_user where `enable` = 1 "
    cur.execute(sql)
    userCount = cur.fetchall()
    print('1',userCount[0][0])
    # ONE_STEP = 50000
    # TOTAL = userCount[0][0]
    ONE_STEP = 100
    TOTAL = 220
    begin = 0
    end = begin + ONE_STEP
    while (end < TOTAL + ONE_STEP):
        print(begin)
        mainIn(begin, ONE_STEP)
        print(end)
        begin += ONE_STEP
        end += ONE_STEP

    cur.close()
    con.commit()
    con.close()
