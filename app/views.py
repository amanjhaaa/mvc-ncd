from app import app

from flask import render_template, request

@app.route("/" , methods = ['GET','POST'])
def home():
    return render_template("index.html")


@app.route("/templates/about.html")
def about():
    return render_template("about.html")



@app.route("/templates/search.html")
def search():
    return render_template("search.html")



@app.route("/templates/contact.html")
def contact():
    return render_template("contact.html")


    
@app.route("/templates/services.html")
def services():
    return render_template("services.html")


 
@app.route("/templates/registration.html")
def registration1():
    return render_template("registration.html")


@app.route('/res',methods=['GET',"POST"])
def res():
 
    return render_template('result1.html')   




@app.route('/login/', methods=['GET',"POST"])
def login():
 
    
    return render_template('ncd1.html')

@app.route('/back',methods=['GET',"POST"])  
def back():  
    if request.method == 'POST':
        return render_template("ncd1.html");  

#back 1 is used for contact.html
@app.route('/back1',methods=['GET',"POST"])  
def back1():  
    if request.method == 'POST':
        return render_template("index.html");  

@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def page_not_found(e):
  
# defining function
  return render_template("404.html"),404



@app.errorhandler(500)
  
# inbuilt function which takes error as parameter
def internal_error(e):
  
# defining function
  return render_template("500.html"),500

