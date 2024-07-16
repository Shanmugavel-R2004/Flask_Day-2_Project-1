from flask import Flask
app=Flask('__name__')
@app.route('/')
def hello():
    return "<h1>Hello 1st page</h1>"
@app.route('/abc')
def hello1():
    return "<h1>It's 2nd page</h1>"
@app.route('/def')
def hello2():
    return "<h1>It's 3rd page</h1>"

if __name__=='__main__':
    app.run(debug=True)