from flask import Flask, jsonify, request

app = Flask(__name__)

contactList = [
     {
        'id': 1,
        'Name': u'Mummm...',
        'Contact': u'9174696547', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Papa :)',
        'Contact': u'9628499100', 
        'done': False
    },
    {
        'id': 3,
        'Name': u'Home Landline',
        'Contact': u'99876444456', 
        'done': False
    },
    {
        'id': 4,
        'Name': u'Dadi',
        'Contact': u'9876543222', 
        'done': False
    },
]

@app.route("/") 
def Homepage():
    return "Welcome to my contacts... :)"

@app.route("/add-data", methods = ["POST"] )
def add_task():
    if not request.json:
        return jsonify({
            "status":"ERRORRR... ⚠️",
            "message": "Please provide the information!"
        },400)

    contacts = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contactList.append(contacts)
    return jsonify({
        "status":"SUCCESS... ✨✨✨",
        "message": "Your contact added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contactList
    }) 

if (__name__ == "__main__"):
    app.run(debug = True)