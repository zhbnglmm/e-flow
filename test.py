from flask import Flask

# 创建一个 Flask 应用
app = Flask(__name__)

# 定义一个路由，当访问根路径时返回 "Hello, World!"
@app.route('/')
def hello():
    return "Hello, World!"

# 启动应用
if __name__ == '__main__':
    app.run()