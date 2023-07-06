#import flask, jsonify and request for developing API
from flask import Flask
from flask import jsonify
from flask import request
#import json to convert object to json
import json

#set app variable
app = Flask(__name__)


#index routeing will make a default JSON data with my name with try catch if the file exist
#it return header and link to different routing
@app.route("/")
def index():

    JSON_data = {
        'Nama' : 'Muhammad Fiqri',
        'Umur' : '19',
        'Hobi' : 'Gaming and Coding',
        'Job Title' : 'Front End Web Dev & Game Dev Freelance'  
    }

    try:
        file = open("data.txt",'x')
        file.write(json.dumps(JSON_data))
        file.close()
    except:
        print("File Already Exist")

    return (
        "<h1>Welcome To My Flask and JSON App<h1/>"
        "<a href='/GetJSON'>Klik Here TO Get JSON API Data<a/> <br>"
        "<a href='/ModifyData'>Klik Here TO Modify JSON Data API<a/>"
    )


#this routing will return the JSON data from the file data.txt
@app.route("/GetJSON", methods=['GET'])
def GetJson():
    if(request.method == 'GET'):
        file = open("data.txt",'r')
        readed_data = file.read()
        file.close()

        return(jsonify(readed_data))


#this routing will return a POST form to modify the JSON data if Request is GET
#if the request POST it will show the modified data
@app.route("/ModifyData", methods=['GET','POST'])
def modifyData():
    if request.method == 'POST':
        Nama = request.form.get('Nama')
        Umur = request.form.get('Umur')
        Hobi = request.form.get('Hobi')
        Job_Title = request.form.get('Job Title')

        JSON_data = {
            'Nama' : Nama,
            'Umur' : Umur,
            'Hobi' : Hobi,
            'Job Title' : Job_Title
        }

        file = open("data.txt",'w')
        file.write(json.dumps(JSON_data))
        file.close()

        file = open("data.txt","r")
        readed_data = file.read()
        file.close()

        return jsonify(readed_data)

    elif request.method == 'GET':
        return '''
            <form method="POST">
                <div><label>Nama: <input type="text" name="Nama"></label></div>
                <div><label>Umur: <input type="text" name="Umur"></label></div>
                <div><label>Hobi: <input type="text" name="Hobi"></label></div>
                <div><label>Job Title: <input type="text" name="Job Title"></label></div>
                <input type="submit" value="Submit">
            </form>'''

#change to debug false when deployed
if __name__ == '__main__':
    app.run(debug=True)