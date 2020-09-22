# -*- coding: UTF-8 -*-
from flask import Flask, render_template,jsonify
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Line
from pyecharts.globals import ChartType, SymbolType
from pyecharts.globals import ThemeType

from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import json


# 案例2：数据逻辑部分
from data_02 import *


# 第一部分：业务逻辑
# 01. 订单量历史数据变化趋势
def hist_order_base():
    dataX, dataY  = order_sum_query()
    # 订单数据
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(dataX)
        .add_yaxis("订单量", dataY, is_smooth=True)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="日订单量历史数据趋势图"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
    )
    return c

# 02：历史数据趋势


