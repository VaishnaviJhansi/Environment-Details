# Refer code for Backend :
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)

# CORS(app) # Enable CORS for all routes and origins



# @app.route('/greet', methods=['POST'])

# def greet():

#   data = request.get_json()
#   name = data.get('name', 'Unknown')
#   greeting = f"Hello, {name}!"
#   return jsonify(greeting=greeting)



# if __name__ == '__main__':
#  app.run(debug=True)









# For passing only one value : environment_details
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask import Flask,app
# from flask import jsonify
# from flask_cors import CORS
# from flask import flash, request
# import mysql.connector
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# CORS(app) # Enable CORS for all routes and origins

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Vaishnavi@1",
#   database="environmentDB"
# )
# mysql = MySQL(app)



# @app.route('/greet', methods=['POST'])
# def greet():
#     data = request.get_json()
#     name = data.get('name', 'Unknown')
#     greeting = f"Hello, {name}!"
#     return jsonify(greeting=greeting)


# @app.route('/post', methods=['POST'])
# def post():
    
#     #data = request.get_json()
#     appln = request.json['appln']
#     cursor = mydb.cursor(dictionary=True)
#     sqlQuery = "INSERT INTO Environment_Details(Appln_Name) VALUES(%s)"
#     cursor.execute(sqlQuery,[appln])
#     mydb.commit()


#     greeting = f"Data added successfully!"
#     return jsonify(greeting=greeting)



# if __name__ == '__main__':
#  app.run(debug=True)








# For passing multiple values : environment_details
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import app
from flask_cors import CORS
from flask import flash, request
import mysql.connector
from flask_mysqldb import MySQL

app = Flask(__name__)

CORS(app) # Enable CORS for all routes and origins

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vaishnavi@1",
  database="environmentDB"
)
mysql = MySQL(app)

cursor = mydb.cursor() 

@app.route('/update/<Appln_Name>', methods=['PUT'])

def update(Appln_Name):

    # Appln = request.json['appln']
    Appln = request.json['Appln_Name']
    Sl = request.json['Sl']
    Env_Level = request.json['Env_Level']
    Infrastructure = request.json['Infrastructure']
    Infra_Type = request.json['Infra_Type']
    Server_Name = request.json['Server_Name']
    Location = request.json['Location']
    Updated_By = request.json['Updated_By']
    Updated_on = request.json['Updated_on']
    Inserted_by = request.json['Inserted_by']
    Inserted_On = request.json['Inserted_On']

    sqlQuery='''UPDATE Environment_Details SET  Sl=%s, Env_Level=%s, Infrastructure=%s, Infra_Type=%s, Server_Name=%s, Location=%s, Updated_By=%s, Updated_on=%s, Inserted_by=%s, Inserted_On=%s where Appln_Name=%s '''
    # binda=(appln,Appln_Desc,OS_1)
    cursor = mydb.cursor() 
    cursor.execute(sqlQuery,[Sl, Env_Level, Infrastructure, Infra_Type, Server_Name, Location, Updated_By, Updated_on, Inserted_by, Inserted_On, Appln])
    mydb.commit()
    return jsonify("data updated successfully")


@app.route('/viewall1', methods =['GET', 'POST'])

def viewall1():   
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("select Appln_Name,Sl,Env_Level,Infrastructure,Infra_Type,Server_Name,Location,Updated_By,Updated_on,Inserted_by,Inserted_On from Environment_Details")
    rows= cursor.fetchall()
    # print (rows)
    return jsonify(rows)


@app.route('/viewall2/<Appln_Name>', methods =['GET'])

def viewall2(Appln_Name):   
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("select Appln_Name,Sl,Env_Level,Infrastructure,Infra_Type,Server_Name,Location,Updated_By,Updated_on,Inserted_by,Inserted_On from Environment_Details")
    rows= cursor.fetchall()
    # print (rows)
    return jsonify(rows)



@app.route('/api/data/<Name>', methods=['GET'])

def get_data(Name):

    # Retrieve data for a specific ID from the database
    # Cursor = mydb.cursor(dictionary=True)
    query = "select * from Environment_Details WHERE Appln_Name= %s"
    cursor.execute(query,[Name])
    data = cursor.fetchone()
    print("Data:",data)
    if data:

        user = {

            'Appln_Name': data[0],
            'Sl': data[1],
            'Env_Level': data[2],
            'Infrastructure': data[3],
            'Infra_Type': data[4],
            'Server_Name': data[5],
            'Location': data[6],
            'Updated_By': data[7],
            'Updated_on': data[8],
            'Inserted_by': data[9],
            'Inserted_On': data[10]

        }
        return jsonify(user)

    else:

        return jsonify({'message': 'Data not found'})


@app.route('/viewall', methods =['GET', 'POST'])

def viewall(): 

 cursor = mydb.cursor(dictionary=True)
 cursor.execute("select* from Environment_Details")
 rows= cursor.fetchall()
 return jsonify(rows)

#      (or)

# @app.route('/viewall', methods =['GET', 'POST'])

# def viewall(): 
#  cursor = mydb.cursor(dictionary=True)
#  cursor.execute("select Appln_Name, Sl, Env_Level, Infrastructure, Infra_Type, Server_Name, Location, Updated_By, Updated_on, Inserted_by, Inserted_On from Environment_Details")
#  rows= cursor.fetchall()
#  return jsonify(rows)


@app.route('/view', methods =['GET', 'POST'])

def view(): 
 mnth=request.json['Appln_Name']
 print(mnth)
 
 sqlQuery="select* from Environment_Details where Appln_Name=%s"
 print("hiii")
 cursor = mydb.cursor(dictionary=True)
 print("hello")
 cursor.execute(sqlQuery,[mnth])
 print("1111")
 value= cursor.fetchall()
 return jsonify(value)

#  sqlQuery="select Appln_Name, Sl, Env_Level, Infrastructure, Infra_Type, Server_Name from Environment_Details where Appln_Name=%s"
#  cursor = mydb.cursor(dictionary=True)
#  cursor.execute(sqlQuery,[mnth])
#  value= cursor.fetchall()
#  return jsonify(value)


# @app.route('/greet', methods=['GET'])
# def greet():
#     # data = request.get_json()
#     # name = data.get('name', 'Unknown')
#     # greeting = f"Hello, {name}!"
#     # return jsonify(greeting=greeting)

#     Inserted_On = request.json['Inserted_On']
#     print("hiiiiii")
#     # select* from Environment_Details

#     cursor = mydb.cursor()
#     print("heloooo")
#     sqlQuery = "select* from Environment_Details"
#     print("aaaaaaaa")
#     //binda=[Appln,Sl,Env_Level,Infrastructure,Infra_Type,Server_Name,Location,Updated_By,Updated_on,Inserted_by,Inserted_On]
#     print(binda)
#     print("azzzzzzz")
#     # cursor.execute(sqlQuery,[appln])
#     cursor.execute(sqlQuery,binda)


@app.route('/post', methods=['POST'])
def post():
    
    #data = request.get_json()
    Appln = request.json['appln']
    Sl = request.json['Sl']
    Env_Level = request.json['Env_Level']
    Infrastructure = request.json['Infrastructure']
    Infra_Type = request.json['Infra_Type']
    Server_Name = request.json['Server_Name']
    Location = request.json['Location']
    Updated_By = request.json['Updated_By']
    Updated_on = request.json['Updated_on']
    Inserted_by = request.json['Inserted_by']
    Inserted_On = request.json['Inserted_On']
    print("hiiiiii")

    cursor = mydb.cursor()
    print("heloooo")
    sqlQuery = "INSERT INTO Environment_Details(Appln_Name, Sl, Env_Level, Infrastructure, Infra_Type, Server_Name, Location, Updated_By, Updated_on, Inserted_by, Inserted_On ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print("aaaaaaaa")
    binda=[Appln,Sl,Env_Level,Infrastructure,Infra_Type,Server_Name,Location,Updated_By,Updated_on,Inserted_by,Inserted_On]
    print(binda)
    print("azzzzzzz")
    # cursor.execute(sqlQuery,[appln])
    cursor.execute(sqlQuery,binda)
    print("yyyyyyyyyyyyyy")

    mydb.commit()
    print("cccccc")

    greeting = f"Data added successfully!"
    return jsonify(greeting=greeting)





if __name__ == '__main__':
 app.run(debug=True)