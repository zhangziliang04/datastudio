# 01.导入文件
from flask import Flask

# 02.创建对象
app = Flask(__name__)


# 03.路由设置
@app.route('/')
# 04.业务逻辑
def hello():
    return '欢迎来到：Python Flask Web 框架基础理论'


# 05. 服务启动
if __name__ == '__main__':
    app.run()
