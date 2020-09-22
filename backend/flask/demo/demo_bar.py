from pyecharts.charts import Bar

# 柱状图对象声明
bar = Bar()

# 参数设置：x轴数据
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# 参数设置：y轴数据
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

# 图表渲染：默认文件命：render.html,默认路径：当前目录
bar.render()
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")