from flask import Flask, render_template, request


application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@application.route('/searchword', methods=['GET', 'POST'])
def search_word():
    return render_template("search_word.html")


if __name__ == '__main__':
    application.run()
