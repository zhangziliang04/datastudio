from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="Flask整合：前后端分离模式"))
    )
    return c


# 数据服务接口：图表
@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


# 首页渲染
@app.route("/")
def index():
    return render_template("index.html")


# 主函数
if __name__ == "__main__":
    app.run()
