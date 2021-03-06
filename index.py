from flask import Flask, request, render_template
import config_flask
from pu.Execute import Execute
import time
from util import db_util

app = Flask(__name__)
app.config.from_object(config_flask)

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'hello world'

@app.route('/execute', methods=['POST'])
def presto_exe():
    exe = Execute()
    exe.creator = request.form['user']
    exe.hql = request.form['hql']
    exe.status = 'new'
    exe.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
    db_util.save_exe(exe)
    return render_template('index.html')

#@app.route('/candles_3ls/<code>')
#def candles_3ls(code):
#    period = request.args.get('type')
#    rs = query_3ls.candles(code, period)
    #print rs
#    return json.dumps(obj = rs)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
