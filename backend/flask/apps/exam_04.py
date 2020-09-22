# 客户地理位置分布图
from pyecharts import options as opts
import pymysql.cursors
from pyecharts.charts import Map

# 案例4：数据逻辑部分
from data_04 import *


# 02: 地图渲染
def customer_order_base():
    dataX, dataY = customer_sum_query()
    # 订单数据
    c = (
        Map(init_opts=opts.InitOpts(width="1200px", height="600px"))
            .add("", [list(z) for z in zip(dataX, dataY)], "world")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="客户地理位置分布图"),
                            visualmap_opts=opts.VisualMapOpts(max_=1600, split_number=8, is_piecewise=True)
                             )

    )
    return c
