#coding=utf-8
import MySQLdb,random,time,hehe
try:
    conn = MySQLdb.Connect(
        port=3306,
        user="root",
        passwd="",
        db="spider",
        charset="utf8"
    )
except:
    print "error_content_to_mysql"
cur=conn.cursor()
#查询数据库数据的总条数
cur.execute("select count(*) from card_province ")
count=cur.fetchall()#返回的结果是一个元组
#先将元组转换成list，然后取list的元组在转换为int得到总的条数
count=int(list(count[0])[0])
number=int(raw_input("请输入需要生成的身份证号数量："))
list_id=xrange(1,count+1)#生成数据库中id的list
random_id=random.sample(list_id,number)#生成N个不重复的id数

def get_date():
    '''

    :return: 返回随机的出生年月
    '''
    # 获取当前的时间戳
    now = long(time.time())
    # 在1970至当前时间生成一个unix时间戳的随机数
    date = random.randint(0, now)
    # 将unix时间戳转换为普通时间
    date = time.gmtime(date)
    return str(time.strftime('%Y%m%d', date))

for i in random_id:
    #得到身份证前六位
    card_id=str(i)
    sql="select card_code from card_province where id= %s"%card_id
    cur.execute(sql)
    data=cur.fetchall()[0]
    data=list(data)
    data=str(data[0])#得到身份证前六位
    card=get_date()#得到身份证的出生年月日
    card=data+card#组装前14位
    num=str(random.randint(100,999))#生成随机三位顺序码，倒数第二位到倒数第四位
    card=card+num #得到身份证前17位
    card=card+hehe.get_check_code(card)
    print card






