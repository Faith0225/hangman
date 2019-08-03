import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='789456',
    db='iris',
    port=3306,
    charset='utf8')
cursor = conn.cursor()
