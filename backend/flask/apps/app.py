from flask import Flask, render_template,jsonify
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Line
from pyecharts.globals import ChartType, SymbolType
from pyecharts.globals import ThemeType

from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import json


from exam_01 import *
from exam_02 import *
from exam_03 import *
from exam_04 import *


app = Flask(__name__, template_folder="../templates", static_folder="../static")


# 第二部分：路由配置
# #############################历史数据查询###########################
# 01. 页面数据请求服务
@app.route("/")
def index():
    cur = rt_index_base()
    # return render_template("dashboard.html", curnumber=cur)
    return render_template("index3.html", curnumber=cur)


# 02. 图表数据查询
@app.route("/histChart")
def get_hist_order_chart():
    c = hist_order_base()
    return c.dump_options_with_quotes()


# 03：订单商品构成模型
# 03-01：页面渲染
@app.route("/bar")
def order_bar():
    cur = rt_index_base()
    return render_template("index5.html", curnumber=cur)


# 03-02：图表数据查询
@app.route("/barChart")
def get_order_chart():
    c = category_order_base()
    return c.dump_options_with_quotes()


# 04：地理位置分布图
# 04.01 页面渲染
@app.route("/map")
def customer_map():
    cur = rt_index_base()
    return render_template("index4.html", curnumber=cur)


# 04.02 图表数据
@app.route("/mapChart")
def get_customer_order_chart():
    c = customer_order_base()
    return c.dump_options_with_quotes()


# 403错误
@app.errorhandler(403)
def miss(e):
    return render_template('error-403.html'), 404


# 404错误
@app.errorhandler(404)
def error(e):
    return render_template('error-404.html'), 500


# 500错误
@app.errorhandler(500)
def error(e):
    return render_template('error-500.html'), 500


# 主函数
if __name__ == "__main__":
    app.run()
    # 模板更改后立即生效
    app.jinja_env.auto_reload = True
    # 代码更改后立即生效
    app.run(DEBUG=True)   # 1.0以后 debug = true不再支持

