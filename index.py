from flask import Flask, request, render_template
import config_flask
import json
import util.db_util

app = Flask(__name__)
app.config.from_object(config_flask)

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'hello world'

@app.route('/execute', methods=['POST'])
def presto_exe():
    print 'post req execute'
    print request.form['user']
    print request.form['hql']
    #db_util.save(hql)
    #return render_template('exe_log.html')

#@app.route('/candles_3ls/<code>')
#def candles_3ls(code):
#    period = request.args.get('type')
#    rs = query_3ls.candles(code, period)
    #print rs
#    return json.dumps(obj = rs)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
