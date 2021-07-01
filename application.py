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
    files = []

    if request.method == 'POST':
        query_word = request.form.get('words')
        with open('static/AliceCleaneredit.txt', 'r') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word1.append(words)

        if query_word in word1:
            movie_title1 = "AliceCleaneredit.txt"
            files.append(movie_title1)

        with open('static/AliceInWonderlandedit.txt', 'r') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word2.append(words)

        if query_word in word2:
            movie_title2 = "AliceInWonderlandedit.txt"
            files.append(movie_title2)

        with open('static/CandideEnedit.txt', 'r') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word3.append(words)

        if query_word in word3:
            movie_title3 = "CandideEnedit.txt"
            files.append(movie_title3)

        with open('static/CandideFredit.txt', 'r') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word4.append(words)

        if query_word in word4:
            movie_title4 = "CandideFredit.txt"
            files.append(movie_title4)

    return render_template("search_word.html", file = files)


if __name__ == '__main__':
    application.run()
