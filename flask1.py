from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/add_two_nums' , methods = ["POST"])
def add_two_nums():
    dataDict = request.get_json()
    return jsonify(dataDict)
    #x = dataDict["x"]
    #y = dataDict["y"]
    #z = x+y
    #retJSON = {
    #    "z":z
    #}

    #return jsonify(retJSON), 200




@app.route('/bye')
def hello_world():
    return "Bye World !!"

@app.route('/prod')
def prod():
    return render_template('index.html')

if __name__=="__main__":
    app.run()
