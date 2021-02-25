from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return 'Halaman Dashboard'

@application.route('/post')
def post():
    return 'Ini Halaman Blog'

@application.route('/comment')
def comment():
    return 'Ini Halaman Comment'

@application.route('/download')
def download():
    return 'Ini Halaman Download'

if __name__ == '__main__':
    application.run(debug=True)