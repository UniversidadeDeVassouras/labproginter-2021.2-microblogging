from flask import Flask, request, render_template

app = Flask(__name__)


class Post:
    def __init__(self, name: str, post: str):
        self.__name = name
        self.__post = post

    def get_name(self):
        return self.__name

    def get_post(self):
        return self.__post


post_list = []


@app.route('/')
def index():  # put application's code here
    return render_template("home.html")


@app.route('/post', methods=['POST'])
def inserir():
    post = Post(request.form['name'], request.form['post'])
    post_list.append(post)
    return render_template("post_list.html", post_list=post_list)


if __name__ == '__main__':
    app.run()
