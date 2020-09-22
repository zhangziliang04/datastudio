##############案例3饼图###################

import pymysql.cursors

# 交易订单量查询
def order_category_sum_query():
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
            # SQL 查询语句：
            sql = "select category_name,count(*)  as 电影类型 from film_information_full group by category_name "
            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []

                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["category_name"])
                    dataY.append(row["电影类型"])
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


