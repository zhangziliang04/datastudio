# 客户地理位置分布图
import pymysql.cursors


# 01-数据查询：不同国家/地区顾客数量
def customer_sum_query():
    # 连接到数据库
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='zhangzl',
                                 db='sakila',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL 查询语句
            sql = "select country,count(distinct rental_id) as customer_num  from customer_address group by country "

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["country"])
                    dataY.append(row["customer_num"])
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()
