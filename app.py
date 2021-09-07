from flask import Flask, url_for
from deploy import views

app = Flask(__name__)

app.add_url_rule('/home', 'home', views.home, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)