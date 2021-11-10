from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


class Post:
    def __init__(self, name: str, post: str):
        self.__name = name
        self.__post = post

    def get_name(self):
        return self.__name

    def get_post(self):
        return self.__post

    def to_dict(self):
        return {
            "name": self.__name,
            "post": self.__post
        }


post_list = []


@app.route('/')
def index():  # put application's code here
    return render_template("home.html")

@app.route("/formulario", methods=['GET'])
def formulario():
    return render_template("formulario.html")

@app.route("/listacompleta", methods=['GET'])
def lista_completa():
    return render_template("post_list.html", post_list=post_list)

@app.route('/post', methods=['POST'])
def inserir():
    post = Post(request.form['name'], request.form['post'])
    post_list.append(post)
    #post_list_dict = []
    #for post in post_list:
    #    post_list_dict.append(post.to_dict())
    #return jsonify(post_list), 201
    return jsonify([post.to_dict() for post in post_list]), 201, {"Content-Type": "application/json"}


if __name__ == '__main__':
    app.run()
