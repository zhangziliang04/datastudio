from pyecharts.charts import Pie
from pyecharts import options as opts
import pymysql.cursors

# 交易订单量查询
def order_category_sum_query():
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


# 执行主函数
if __name__ == '__main__':
    print(order_category_sum_query())
    dataX, dataY = order_category_sum_query()
    data_pair = [list(z) for z in zip(dataX, dataY)]
    pie = Pie()
    pie.add("", data_pair)
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="商品类型构成图"),
        legend_opts=opts.LegendOpts(
            orient="vertical",
            pos_top="15%",
            pos_right="-4.5%"),
    )
    pie.set_series_opts(label_opts= opts.LabelOpts(formatter="{b}: {c} ({d}%)"),
                        position="outside",
                        background_color = "#eee",
                        border_color="#aaa",
                        border_width=1,
                        border_radius=4
                     )
    pie.render('pie.html')
