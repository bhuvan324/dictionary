from flask import Flask, render_template, url_for, request,redirect
from managers import Dictionary
app=Flask(__name__)
dic=Dictionary()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/<name>')
@app.route('/about/')
def about(name=''):
    if name=='':
        name='Buddy'
    message={'greet':f'Hello {name}.'}
    return render_template('about.html',message=message)

@app.route('/result', methods=['GET','POST'])
def result():
    print('from result')
    if request.method=='POST' and request.form['word']!= "":
        word=request.form['word']
        c=dic.definition(word)
        de={'word':word, 'data':c[1:],'numbering':1, 'intro':c[0]}
        print(de)
        return render_template('home.html',dr=de)

    return render_template('home.html')

if __name__ =='__main__':
    app.run(debug=True)
