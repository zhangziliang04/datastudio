# 定时增量数据更新示例
from random import randrange
from flask.json import jsonify
from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Line

# 01-创建一个Flask应用
app = Flask(__name__, static_folder="templates")


# 02-图表对象配置项参数设置
def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="定时增量更新图表"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line


# 页面-路由设置
@app.route("/")
def index():
    return render_template("index3.html")


# 数据-图表配置属性参数：路由设置
@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()


idx = 9


# 数据-图表数据属性配置项更新：路由设置
@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})


# 主函数
if __name__ == "__main__":
    app.run()
