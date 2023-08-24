from mysql.connector import errorcode
from createconnection import createcon

cnx=createcon("localhost","root","")
cursor=cnx.cursor(dictionary=True)
quary1='select city.ID,CITY.Name from world_x.city'
#quary2='insert into compony.order_prep select orders.order_id,orders.staff_id from production.orders'
#quary2='select * from compony.order_prep'
cursor.execute(quary1)
result = cursor.fetchall()
for rows in result:
 print(rows)
 insQryWInfo = "insert into practice1.world_info (id,Name) values({},{}) ".format(rows['id'],rows['Name'])
 insQryCountry = "insert into practice1.country (id,Name) values ({},{}) ".format(rows['id'],rows['Name'])
 genericinsert(insQryWInfo)
 genericinsert(insQryCountry)


 def genericinsert(qry):
    print("query is ",qry)
    cursor.execute(qry)
    cnx.commit()