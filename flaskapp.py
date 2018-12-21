from flask import Flask, request, jsonify
import os 
app = Flask(__name__)
@app.route('/getData', methods=['GET'])
def parse_request():
    for key in request.args:
        value = request.args[key]
        print(key+ ' - '+ value)
        ob ={'foo':'bar'} 
    return jsonify(ob) 
if __name__ == "__main__":
    server_port = os.environ['SERVER_PORT']
    print(server_port)
    app.run(host='127.0.0.1', port=server_port , debug=True)
