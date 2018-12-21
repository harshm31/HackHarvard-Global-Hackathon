from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/getData', methods=['GET'])
def parse_request():
    for key in request.args:
        value = request.args[key]
        print(key+ ' - '+ value)
        ob ={'foo':'bar'} 
    return jsonify(ob) 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
