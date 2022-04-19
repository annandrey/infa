import flask
from flask import Flask, request
app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")
@app.route('/hello/<string:text>')
@app.route('/hello')
def hello_world(text=None):
    return 'Just a plain text: "Hello from Flask!"' + (' With path .../' + text if text else '')
@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )
@app.route('/name', methods = ['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        name_param=request.args.get('name')
    elif request.method == 'POST':
        name_param=request.form.get('name')

    if name_param is None:
        name_param="Ошибка"
    else:
        name_param = name_param[ : :-1]
    return flask.render_template(
        'name.html',
        name=name_param,
        method=request.method
    )
NICE_PICS = ["pics/frog1.jpg", "pics/frog3.jpg", "pics/frog4.jpg", "pics/frog5.jpg", "pics/imposter_frog.jpg"]
@app.route('/number', methods = ['GET'])
def number():
    if request.method == 'GET':
        number_param = request.args.get('number')
    if number_param is None:
        number_param = 0
    else:
        number_param = int(number_param[0])
    number_param %= 5
    pics = NICE_PICS[number_param]
    return flask.render_template(
        'number.html', 
        pics = pics
    )
if __name__ == '__main__':
   app.run(debug = True)
