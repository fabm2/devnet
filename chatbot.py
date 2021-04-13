import flask
import requests

accesstoken = 'YjMxNzcwZTItYzQ5YS00MTAzLTg4NDYtOTExODUzZWQwMzk4ZWYxMWQzODctYzcx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

# username botzito@webex.bot
# botid Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzFhM2UwNmQwLTc4Y2ItNDJkNS04ZDdjLTNiMGJiMDkxNTk4Mw

ngrok = 'http://8ee0614191f3.ngrok.io'

from flask import Flask

from flask import Flask  # import flask

app = Flask(__name__)  # create an app instance


@app.route("/")  # at the end point /
def hello():  # call method hello
    print("Hello World!")  # which returns "hello world"


if __name__ == "__main__":  # on running python app.py
    app.run(port=5005)  # run the flask app
