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


@app.route('/greet', methods=['GET'])
def greet():
    # data = request.get_json()
    # name = data.get('name', 'Unknown')
    # greeting = f"Hello, {name}!"
    # return jsonify(greeting=greeting)

    Inserted_On = request.json['Inserted_On']
    print("hiiiiii")
    # select* from Environment_Details

    cursor = mydb.cursor()
    print("heloooo")
    sqlQuery = "select* from Environment_Details"
    print("aaaaaaaa")
    binda=[Appln,Sl,Env_Level,Infrastructure,Infra_Type,Server_Name,Location,Updated_By,Updated_on,Inserted_by,Inserted_On]
    print(binda)
    print("azzzzzzz")
    # cursor.execute(sqlQuery,[appln])
    cursor.execute(sqlQuery,binda)


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