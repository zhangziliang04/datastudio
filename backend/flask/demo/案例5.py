################案例5################
from pyecharts import options as opts
import pymysql.cursors
from pyecharts.charts import Bar

# 不同门店的营业额
def month_store_query():
    # 连接到数据库
    connection = pymysql.connect(host='111.231.196.162',
                                 port=3306,
                                 user='root',
                                 password='zhangzl',
                                 db='sakila',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL 查询语句
            sql = "select * from month_store_amount "

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                dataX = []
                dataY1 = []
                dataY2 = []
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    dataX.append(row["payment_date"])
                    dataY1.append(row["A"])
                    dataY2.append(row["B"])
                return dataX, dataY1, dataY2
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()

# 执行主函数
if __name__ == '__main__':
    print(month_store_query())
    dataX, dataY1, dataY2 = month_store_query()
    bar = Bar()
    bar.add_xaxis(dataX)
    bar.add_yaxis("A", dataY1)
    bar.add_yaxis("B", dataY2)
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(type_="category"),
                        yaxis_opts=opts.AxisOpts(type_="value"),
                        title_opts={"text":"商店盈利能力分析图","subtext":"单位（美元）"})
    bar.render('store_amount.html')

