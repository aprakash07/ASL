from flask import Flask,request,render_template
import os
from app2 import applicat
app = Flask(__name__)

@app.route('/')

def index():
    
    return render_template("reg.html")



@app.route('/form_reg', methods=['POST','GET'])
def submit():
    applicat()
    return render_template("reg.html")
    
    
if __name__ =="__main__":
    app.run()