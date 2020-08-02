import pymysql as mdb


def mainIn(begin, step):
    path='orgMember.txt'
    file= open(path,"a+",encoding='utf-8')
    sql = "SELECT corp_id,user_id, `name`, (case WHEN user_state&16=16 THEN 0 else 1 END)AS isactive,email,(case WHEN (user_state&64=64) || (user_state=0) THEN 0 else 1 END)AS allLogin,fixed_phone,created,position,authority FROM t_corporation_user WHERE user_state&1=1   limit " +str(begin)+ ","+ str(step)
    cur.execute(sql)
    rows = cur.fetchall()
    corpId=''
    userId=''
    phone=''
    name=''
    isActive=''
    enableLogin=''
    email=''
    created=''
    fixedPhone=''
    userType='0'
    authority='1'
    position='1'
    j=0
    for row in rows:
        i=0
        for r in row:
            if(i==0):
                corpId=str(r)
            elif(i==1):
                userId=str(r)
                phone=getPhone(userId)
                userType=getUserType(corpId, userId)
            elif(i==2):
                name=str(r).replace("\r","").replace("\n","")
            elif(i==3):
                isActive=str(r)
            elif(i==4):
                email=str(r).replace("\r","").replace("\n","")
            elif(i==5):
                enableLogin=str(r)
            elif(i==6):
                fixedPhone=str(r).replace("\r","").replace("\n","")
            elif(i==7):
                created=str(r)
            elif(i==8):
                position=str(r)
            elif(i==9):
                authority=str(r)
            i=i+1
        j=j+1
        print(j, corpId+'$'+phone+'$'+'*'+userId)
        if(phone==''):
            continue
        else:
            file.write(corpId+'$'+phone+'$'+name+'$'+isActive+'$'+email+'$'+enableLogin+'$'+fixedPhone+'$'+created+'$'+userType+'$'+position+'$'+authority)
            file.write('\n')
    print('total:',len(rows))
    return 0;

def getPhone(userId):
    sql = "SELECT phone FROM t_corporation_user WHERE user_id=" + userId + " limit 1"
    cur.execute(sql)
    rows = cur.fetchall()
    if(len(rows)==0):
        return ''
    else:
        return str(rows[0][0])

def getUserType(corpId, userId):
    sql = "SELECT admin_type FROM t_corporation_admin WHERE `enable`=1 AND (admin_type=1 OR admin_type=4) AND user_id="+userId+" and corp_id="+corpId
    cur.execute(sql)
    rows = cur.fetchall()
    if(len(rows)==0):
        return '0'
    else:
        type=str(rows[0][0])
        if(type=='1'):
            return '2'
        elif(type=='4'):
            return '1'
        else:
            return '0'
if __name__=='__main__':
    con = mdb.connect("localhost", "root", "werered", "test", charset='utf8')
    cur = con.cursor()
    sql = "SELECT count(*) FROM t_corporation_user"
    cur.execute(sql)
    userCount = cur.fetchall()
    ONE_STEP = 100000
    TOTAL = userCount[0][0]
    # TOTAL = 120
    begin = 0
    end = begin + ONE_STEP
    while (end < TOTAL + ONE_STEP):
        print(begin)
        mainIn(begin, ONE_STEP)
        print(end)
        begin += ONE_STEP
        end += ONE_STEP

    cur.close()
    con.close()