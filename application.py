from flask import Flask, render_template, request


application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@application.route('/searchword', methods=['GET', 'POST'])
def search_word():
    word1 = []
    word2 = []
    word3 = []
    word4 = []
    with open('static/AliceCleaneredit.txt', 'r', encoding="utf-8-sig") as fileinput:
        for line in fileinput:
            for words in line.split():
                word1.append(words)

    with open('static/AliceInWonderlandedit.txt', 'r', encoding="utf-8-sig") as fileinput:
        for line in fileinput:
            for words in line.split():
                word2.append(words)

    with open('static/CandideEnedit.txt', 'r', encoding="utf-8-sig") as fileinput:
        for line in fileinput:
            for words in line.split():
                word3.append(words)

    with open('static/CandideFredit.txt', 'r', encoding="utf-8-sig") as fileinput:
        for line in fileinput:
            for words in line.split():
                word4.append(words)
    return render_template("search_word.html", word1 = word1, word2 = word2, word3 = word3, word4 = word4)


if __name__ == '__main__':
    application.run()
