from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))

msg = 'Python say "Hello World"'
c = len(msg) + 4
print("+" * c)
print("+", msg, "+")
print("+" * c)
