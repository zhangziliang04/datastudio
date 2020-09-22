#############案例4#####################
from pyecharts import options as opts
import pymysql.cursors
from pyecharts.charts import Map



# 不同国家/地区顾客数量
def customer_sum_query():
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


# 执行主函数
if __name__ == '__main__':
    print(customer_sum_query())
    dataX, dataY = customer_sum_query()
    map = Map(init_opts=opts.InitOpts(width="1200px", height="600px"))
    map.add("", [list(z) for z in zip(dataX, dataY)], "world")
    map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    map.set_global_opts(title_opts=opts.TitleOpts(title="客户地理位置分布图"),
                        visualmap_opts=opts.VisualMapOpts(max_=1600, split_number=8, is_piecewise=True)
                        )

    map.render( "customer_address.html")