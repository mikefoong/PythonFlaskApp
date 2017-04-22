from flask import Flask,render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.MachineData

@app.route('/')
def showMachineList():
    return render_template('list.html')

@app.route('/addMachine', methods=['POST'])
def addMachine():
    try:
        json_data = request.json['info']
        deviceName = json_data['device']
        ipAddress = json_data['ip']
        userName = json_data['username']
        password = json_data['password']
        portNumber = json_data['port']

        db.Machine.insrt_one({
            'device':deviceName, 'ip':ipAddress, 'username':userName, 'password':password, 'port':portNumber
        })
        return jasonify(status='OK',message='inserted successfully')

    except Exception as e:
        return jasonify(status='ERROR', message=str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
