#############案例6################
from pyecharts import options as opts
import pymysql.cursors
from pyecharts.charts import Radar
from pyecharts.globals import ThemeType


# 不同门店的营业额
def store_query():
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
            sql = "select * from store_all "

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                data1 = []
                data2 = []
                data3 = []
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    data1.append(row["A"])
                    data2.append(row["B"])
                    data3.append(row["category"])
                return data1, data2, data3
            except:
                print("错误：数据查询操作失败")
    finally:
        connection.close()
# 执行主函数
if __name__ == '__main__':
    print(store_query())
    data1, data2, data3 = store_query()
    radar = Radar(init_opts=opts.InitOpts(theme=ThemeType.DARK,width="1280px", height="720px"))
    radar.add_schema(schema=[
        opts.RadarIndicatorItem(name="门店订单金额", max_=50000),
        opts.RadarIndicatorItem(name="门店订单量", max_=10000),
        opts.RadarIndicatorItem(name="门店顾客数", max_=10000),
        opts.RadarIndicatorItem(name="门店商品类型", max_=10000),
    ],
    splitarea_opt=opts.SplitAreaOpts(
    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
    ),
    textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
    radar.add(series_name="1号门店",
              data=[list(data1)],
              linestyle_opts=opts.LineStyleOpts(color="#CD0000")
              )
    radar.add(series_name="2号门店",
              data=[list(data2)],
              linestyle_opts=opts.LineStyleOpts(color="#5CACEE")
              )
    radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    radar.set_global_opts(
        title_opts=opts.TitleOpts(title="门店竞争优势多维分析"), legend_opts=opts.LegendOpts()
    )
    radar.render('radar.html')
