
from code1 import ocr
from flask import Flask
import json 
from flask import  request, jsonify

app = Flask(__name__)

@app.route('/search/text/',  methods=['POST'])
def category_l1():
    try:  
        #print(request.data)
        param = json.loads(request.data)
        #print("after param",param['position'])
        #print(len(param['position']))
        if param['file_name'].endswith('.csv'):
            pass
        else:
            raise
    except:
        return "Please provide csv file only and provide correct co-ordinates in format"+' '+"[x0,y0,x2,y2]"
    else:
        result=ocr(param['file_name'],param['position'])
        
    return jsonify({"text":result})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,use_reloader=False,threaded=False)