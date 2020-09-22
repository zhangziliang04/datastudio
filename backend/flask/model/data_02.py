# -*- coding: UTF-8 -*-
# 历史数据趋势
import pymysql.cursors

# 交易额查询
def pay_sum_query():
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
            sql = "SELECT * FROM dm_payment_day ORDER BY 日期 DESC"

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["日期"])
                    dataY.append(row["金额"])
                    # 打印结果

                    return dataX, dataY
            except:
                print("错误：数据查询操作失败")
            print("日期：%s,交易额：%.2f" % (dataX, dataY))
    finally:
        connection.close()


# 交易订单量查询
def order_sum_query():
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
            sql = "SELECT * FROM dm_rental_day ORDER BY 日期 ASC "
            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY = []

                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["日期"])
                    dataY.append(row["订单量"])
                return dataX, dataY
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


# 执行主函数
if __name__ == '__main__':
    print(order_sum_query())
