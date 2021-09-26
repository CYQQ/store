import pymysql
host='localhost'
database='company'
user='root'
password="0"
def update(sql,param) :
    con = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def select(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(sql, param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    con.commit()
    cursor.close()
    con.close()
