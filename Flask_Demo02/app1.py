from flask import Flask,url_for,render_template

# 将当前运行的主程序构建成Flask应用,以便接收用户的请求(request)和响应(response)
app = Flask(__name__)


@app.route('/01-var')
def var_views():
    name = '隔壁老王'
    age = 32
    salary = 125.55
    tup=('老魏','老王','老吕','小蒙蒙')
    list = ['漩涡鸣人','宇智波佐助','春野樱']
    dic = {
        'C':'CHINA',
        'A':'AMERICA',
        'J':'JAPAN',
    }
    dog = Dog()

    return render_template('01-var.html',params=locals())


class Dog(object):
    name = '旺财'
    def eat(self):
        return self.name + '吃狗粮'
    



if __name__ == '__main__':
    # 运行Flask应用(启动Flask服务),默认会在本机开启5000端口,允许使用http://localhost:5000
    # 访问Flask的web应用
    # debug=True,将运行模式更改为调试模式(开发环境中推荐使用True,生产环境必须改为False)
    app.run(debug=True,port=5500)
    # 可在app.run中添加port参数,host参数 ,可修改端口号,默认为5000
