from flask import Flask

# 将当前运行的主程序构建成Flask应用,以便接收用户的请求(request)和响应(response)
app = Flask(__name__)


if __name__ == '__main__':
    