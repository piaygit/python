#-*- coding=utf-8 -*-
import public_method,random
conn=public_method.content_mysql()
cur=conn.cursor()
cur.execute("select count(*) from provinces")
count=cur.fetchall()#查询结果是一个包含元祖：[(),()]这样的一个list
count=list(count[0])
count=int(count[0])#得到总行数
number=int(raw_input("请输入需要生成的身份证个数："))
list_id=xrange(1,count+1)#生成数据库id的一个序列
random_id=random.sample(list_id,number) #生成不重复的id
for i in random_id:
    sql="select provinces_code_card from provinces where id = %d"%i
    cur.execute(sql)
    data_id=cur.fetchall()
    data_id=list(data_id[0])
    card=str(data_id[0])#得到前六位
    card=card+public_method.get_random_date()#得到前14位
    num=str(random.randint(100,999))#生成顺序位的3位即：倒数第二到倒数第四位
    card=card+num
    last_cardnumber=public_method.get_last_number(card)#得到最后一位校验位
    card=card+last_cardnumber
    print card