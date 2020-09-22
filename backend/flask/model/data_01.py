# -*- coding: UTF-8 -*-
# 指标卡数据
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
            # SQL 查询语句：简化程序只返回第一行
            sql = "SELECT * FROM dm_payment_day ORDER BY 日期 DESC limit 1 "

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    paydate = row["日期"]
                    paysum = row["金额"]
                    # 打印结果
                    print("日期：%s,交易额：%.2f" % (paydate, paysum))
                    return paysum
            except:
                print("错误：数据查询操作失败")

    finally:
        connection.close()


# 交易量查询
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
            # SQL 查询语句：简化程序只返回第一行
            sql = "SELECT * FROM dm_rental_day ORDER BY 日期 DESC limit 1 "
            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    orderdate = row["日期"]
                    ordersum = row["订单量"]
                    # 打印结果
                    print("日期：%s,交易额：%d" % (orderdate, ordersum))
                    return ordersum
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


# 库存量
def inventory_sum_query():
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
            # SQL 查询语句：简化程序只返回第一行
            sql = "SELECT * FROM dm_inventory_day ORDER BY 日期 DESC limit 1 "

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    inventdate = row["日期"]
                    inventsum = row["库存量"]
                    # 打印结果
                    print("日期：%s,交易额：%d" % (inventdate, inventsum))
                    return inventsum
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()


# 执行主函数
if __name__ == '__main__':
    print(pay_sum_query())
    print(order_sum_query())
    print(inventory_sum_query())
