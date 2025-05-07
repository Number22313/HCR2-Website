from flask import Flask,render_template


app = Flask(__name__)


#make home.html the first page to load
@app.route('/')
def home():
    return render_template('home.html')


#enable debugging
if __name__ == '__main__':
    app.run(debug = True)


#database example code
#@app.route('/page_1/<int:id>')
#def page_1():
#   return render_template('page_1.html')