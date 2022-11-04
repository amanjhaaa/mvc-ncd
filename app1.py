from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from random import randint


# import json
app = Flask(__name__)#interface between webserver and web application

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'aman1'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'aman'
 

mysql = MySQL(app)


firstname = " "
add = 0
result = " "
age = ""
smoke = ""
alcohol = ""
measurement = ""
physical = ""
disease_family_hist = ""
patient_id = " "

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


# route to get data from html form and insert data into database
@app.route('/registration', methods=["GET", "POST"])
def registration():
    global patient_id
    global firstname
    middlename = " "
    lastname = " "
    email = " "
    gender = " "
    birthday = " "
    pincode = " "

    patient_id = randint(10000000000000,99999999999999)

    if request.method == "POST":
    
        firstname = request.form['fname']
        middlename = request.form['mname']
        lastname = request.form['lname']
        email =  request.form['email']
        gender = request.form['gender']
        birthday = request.form['birthday']
        pincode = request.form["pincode"]
        


        cursor = mysql.connection.cursor()

        cursor.execute(''' INSERT INTO patient_info VALUES(%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(patient_id,firstname,middlename,lastname,email,gender,birthday,pincode,age,smoke,alcohol,measurement,physical,disease_family_hist,add,result))
        mysql.connection.commit()
        
   
    return render_template("ncd1.html",patientid = patient_id , fname = firstname,mname= middlename,lname =  lastname,email1 = email,gender1 = gender,birthday1 = birthday,pincode1 = pincode)


@app.route('/res',methods=['GET',"POST"])
def res():
 
    return render_template('result1.html')   




@app.route('/login/', methods=['GET',"POST"])
def login():
 
    
    return render_template('ncd1.html')

@app.route('/result1',methods=['GET',"POST"])
def result1():
    if request.method == "POST":
        count = 0

# getting the value for age

        while True :
            global age 
            global smoke 
            global alcohol 
            global measurement
            global physical 
            global disease_family_hist

        
            age = request.form['age']
            
            smoke = request.form['smoke']
            
            alcohol =request.form['alcohol']

            
            measurement = request.form['measurement']
            
            physical =  request.form['physical']



            disease_family_hist =  request.form['history']
        

            count = int(age)+int(smoke)+int(alcohol)+int(measurement)+int(physical)+int(disease_family_hist)
            
            global add 
            add = count
            print(add)
            global result
            if count>4:
                result="you need screening" 

                
 
            else:
                result="No screening needed"
 

            cursor = mysql.connection.cursor()

            query = 'UPDATE patient_info SET age  = %s,smoke = %s,alcohol = %s,measurement = %s,physical = %s,disease_family_hist = %s,count = %s,result = %s WHERE firstname = %s'
            value = (age,smoke,alcohol,measurement,physical,disease_family_hist,add,result,firstname)
            cursor.execute(query,value)
            mysql.connection.commit()
            cursor.close()

            return render_template('result1.html', add1=add,prescription=result)
    return render_template('result1.html', add1="result not found in session.")

@app.route('/back',methods=['GET',"POST"])  
def back():  
    if request.method == 'POST':
        return render_template("ncd1.html");  

#back 1 is used for contact.html
@app.route('/back1',methods=['GET',"POST"])  
def back1():  
    if request.method == 'POST':
        return render_template("index.html");  





@app.route("/searching1", methods=['GET', 'POST'])
def searching():
    if request.method == 'POST':
        x = request.form['patient if']
    
        query =  "SELECT * FROM patient_info WHERE patientid LIKE '%"+x+"%'OR firstname LIKE '%"+x+"%'"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        print(data)
        return render_template("search.html",data = data)
       
if __name__ == '__main__':

  
    app.run(debug=True)