# 案例3：订单商品构成模型
from pyecharts.charts import Pie
from pyecharts import options as opts

# 案例3：数据逻辑部分
from data_03 import *


# 业务逻辑
# 02: 地图渲染
def category_order_base():
    dataX, dataY = order_category_sum_query()
    data_pair = [list(z) for z in zip(dataX, dataY)]
    # 订单数据
    c = (
        Pie()
        .add("", data_pair)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="商品类型构成图"),
            legend_opts=opts.LegendOpts(
                orient="vertical",
                pos_top="15%",
                pos_right="-4.5%"),
        )
        .set_series_opts(label_opts= opts.LabelOpts(formatter="{b}: {c} ({d}%)"),
                            position="outside",
                            background_color = "#eee",
                            border_color="#aaa",
                            border_width=1,
                            border_radius=4
                         )
            )
    return c

