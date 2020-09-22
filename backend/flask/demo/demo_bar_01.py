from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


from pyecharts.globals import ThemeType

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT,
                                width="1024px",
                                height="600px",

                                bg_color="#d9d6c3"
                                ))
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .render("demo_bar_01.html")
)
