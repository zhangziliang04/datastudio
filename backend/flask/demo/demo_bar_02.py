from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="图表标题",
                                  title_link="www.baidu.com",
                                  title_target="blank",
                                  subtitle="图表副标题",
                                  subtitle_link="www.baidu.com",
                                  subtitle_target="blank",
                                  pos_left="left",
                                  # pos_right="",
                                  # pos_bottom="40",
                                  padding=[5, 10, 5, 10])   # 上右下左
    )
    .render("demo_bar_02.html")
)