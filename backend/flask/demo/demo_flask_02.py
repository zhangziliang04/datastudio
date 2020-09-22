from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # 变量
    my_str = '我是字符串变量'
    my_int = 8888
    return render_template('hello.html',
                           my_str=my_str,
                           my_int=my_int
                           )


if __name__ == '__main__':
    app.run(debug=True)
