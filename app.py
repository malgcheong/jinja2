from flask import Flask, render_template
app = Flask(__name__)

# Jinja2 예시
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

items = [{'title':'제목1', 'content':'내용1'}, {'title':'제목2', 'content':'내용2'}, {'title':'제목3', 'content':'내용3'}]
user = {'logged_in' : 3, 'username' : '남청우'}

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template("template.html")
rendered_template = template.render(title='제목', content='내용', items=items, user = user)
print(rendered_template)

@app.route('/')
def home():
   return rendered_template

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)
