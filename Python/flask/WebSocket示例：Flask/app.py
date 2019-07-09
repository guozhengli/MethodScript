from flask import Flask,request,render_template,session,redirect
import uuid
import json
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer


app = Flask(__name__)
app.secret_key = 'asdfasdf'

GENTIEMAN = {
    '1':{'name':'钢弹','count':0},
    '2':{'name':'铁锤','count':0},
    '3':{'name':'闫帅','count':0},
}

WEBSOCKET_DICT = {

}

@app.before_request
def before_request():
    if request.path == '/login':
        return None
    user_info = session.get('user_info')
    if user_info:
        return None
    return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        uid = str(uuid.uuid4())
        session['user_info'] = {'id':uid,'name':request.form.get('user')}
        return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html',users=GENTIEMAN)

@app.route('/message')
def message():
    # 1. 判断到底是否是websocket请求？
    ws = request.environ.get('wsgi.websocket')
    if not ws:
        return "请使用WebSocket协议"
    # ----- ws连接成功 -------
    current_user_id = session['user_info']['id']
    WEBSOCKET_DICT[current_user_id] = ws
    while True:
        # 2. 等待用户发送消息，并接受
        message = ws.receive() # 帅哥ID
        # 关闭：message=None
        if not message:
            del WEBSOCKET_DICT[current_user_id]
            break

        # 3. 获取用户要投票的帅哥ID,并+1
        old = GENTIEMAN[message]['count']
        new = old + 1
        GENTIEMAN[message]['count'] = new

        data = {'user_id': message, 'count': new,'type':'vote'}
        # 4. 给所有客户端推送消息
        for conn in WEBSOCKET_DICT.values():
            conn.send(json.dumps(data))
    return 'close'

@app.route('/notify')
def notify():
    data = {'data': "你的订单已经生成，请及时处理；", 'type': 'alert'}
    print(WEBSOCKET_DICT)
    for conn in WEBSOCKET_DICT.values():
        conn.send(json.dumps(data))
    return '发送成功'

if __name__ == '__main__':
    http_server = WSGIServer(('192.168.11.143', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()