# import MySQLdb as mdb
import pymysql as mdb


def mainIn():
    path='org.txt'
    file= open(path,"w",encoding='utf-8')
    sql = "SELECT 0 AS isboss, NULL AS bind_boss_account, t.corp_id ,t.`name`, t.city, 'A' AS industry, created FROM t_corporation t  WHERE t.`enable`=1 and t.province=50"
    cur.execute(sql)
    rows = cur.fetchall()
    isboss=''
    bind_boss_account=''
    corp_id=''
    name=''
    county=''
    industry=''
    created=''
    j=0
    for row in rows:
        i=0
        for r in row:
            if(i==0):
                isboss=str(r)
            elif(i==1):
                bind_boss_account=str(r)
            elif(i==2):
                corp_id=str(r)
            elif(i==3):
                name=str(r).replace("\r","").replace("\n","")
            elif(i==4):
                county=str(r).replace("\r","").replace("\n","")
            elif(i==5):
                industry=str(r).replace("\r","").replace("\n","")
            elif(i==6):
                created=str(r).replace("\r","").replace("\n","")
            i=i+1
        j=j+1
        print(j, corp_id)
        file.write(isboss+'$'+bind_boss_account+'$'+corp_id+'$'+name+'$'+county+'$'+industry+'$'+created)
        file.write('\n')
    print('total:',len(rows))
    return 0;
if __name__=='__main__':
    con = mdb.connect(host='127.0.0.1', port=33601, user='wangsheng', passwd='cmcc1234', db="littlec_user",charset='utf8')
    cur = con.cursor()
    mainIn()
    cur.close()
    con.close()