from flask import Flask, request,render_template #import main Flask class and request object
import json
import requests

app = Flask(__name__) #create the Flask app

es_index = "product_name"

@app.route('/')
def home():
    return render_template("a.html")

@app.route('/es',methods=['GET', 'POST'])
def query_example():
    product = request.args.get("product")
    if product:
       data={"suggest":{"product-suggest":{"prefix": product,"completion":{"field":"name.completion"}}}}
       #data={"suggest":{"product-suggest":{"match": product,"completion":{"field":"name.edgengram"}}}}
       #data={"suggest":{"product-suggest":{"match": {"name.edgengram": product}}}}
       header = {"Content-Type": "application/json"}
       r=requests.post("http://localhost:9200/%s/_search" % es_index,data=json.dumps(data),headers=header)

       result = [i['_source']['name'] for i in json.loads(r.text)['suggest']['product-suggest'][0]['options']]
       return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=80) #run app in debug mode on port 5000
