from flask import Flask,request,render_template,session,redirect

app = Flask(__name__)


@app.route('/login')
def login():
    import sql_helper
    result = sql_helper.fetch_one('select * from user where name=%s and pwd=%s ',['alex','123'])
    print(result)
    return 'Login'

@app.route('/index')
def index():
    import sql_helper
    result = sql_helper.fetch_all('select * from user',[])
    print(result)
    return "Index"

@app.route('/host')
def host():
    pass


if __name__ == '__main__':
    app.run()
