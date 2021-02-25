from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return 'Halaman Dashboard'

@application.route('/post')
def post():
    return 'Ini Halaman Blog'

if __name__ == '__main__':
    application.run(debug=True)