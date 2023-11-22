#importing template by module of render_template and request to server
from flask import Flask,request, render_template

app=Flask(__name__)

@app.route('/')

def welcome():
  return render_template('post.html')



@app.route('/login',methods=['POST'])

def login():
     # Retrieve "uname" and "password" parameters from the form data.
    username=request.form.get('uname')
    password=request.form.get('pass')
    if username=='Galax' and password=='gm12345':
        return 'Welcome %s' %username
    else:
        return "Wrong Credentials"
    
if __name__=='__main__':
    app.run(debug=True)