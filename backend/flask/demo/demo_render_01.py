from pyecharts.charts import Bar

# 导出图片，需要引入以下对象
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
# 默认模式
bar.render()
# 指定文件名（可以包括路径）
bar.render("mycharts.html")

# 渲染成图片
make_snapshot(snapshot, bar.render(), "bar0.png")
