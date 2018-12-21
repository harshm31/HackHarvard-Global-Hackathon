from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import sys
sys.path.insert(0,'../ClimateNews')
import news_json_parser as njp 
import os 

app = Flask(__name__)
@app.route('/getNews', methods=['GET'])
def parse_request():
    #for key in request.args:
     #   value = request.args[key]
      #  print(key+ ' - '+ value)
       # ob ={'foo':'bar'} 
    #return jsonify(ob)
    #code to scrape data from website 
    url = "https://insideclimatenews.org/todaysclimate"
    req = requests.get(url , verify = False)
    soup = BeautifulSoup(req.content,"lxml")

    try :
        output=njp.get_json_output(soup)
        return output
    except Exception as e :
        return e
if __name__ == "__main__":
    server_port = os.environ['SERVER_PORT']
    print(server_port)
    app.run(host='127.0.0.1', port=server_port , debug=True)
