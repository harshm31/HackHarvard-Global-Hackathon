from flask import Flask, request, jsonify
import urllib.request
from bs4 import BeautifulSoup
import sys
sys.path.insert(0,'../ClimateNews')
import news_json_parser as njp
import os 

app = Flask(__name__)
@app.route('/getNews', methods=['GET'])
def parse_request():
    url = "https://insideclimatenews.org/todaysclimate"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    soup = BeautifulSoup(response,"lxml")

    output=njp.get_json_output(soup)
    return output

if __name__ == "__main__":
    server_port = os.environ['SERVER_PORT']
    print(server_port)
    app.run(host='127.0.0.1', port=server_port , debug=True)
