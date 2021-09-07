from flask_api import FlaskAPI
from flask import request
import json

app = FlaskAPI(__name__)

@app.route('/hello')
def example():
    return {"hello" : "world"}

@app.route('/mhlw/category/')
def getqa():
    return "your get request allowed"

@app.route('/mhlw/category/list', methods=['GET'])
def showFAQ(qid):
    #stub = makeStub()
    qaJson={}
    tags=[]
    with grpc.insecure_channel('faq-grpc:50051') as channel:
        stub = FaqGatewayStub(channel)
        # get qa from grpc server
        response = faq_client.show_qa(stub, qid)
        print(type(response))
        print(response)
        qaJson["QID"]=response.QID
        qaJson["serviceName"]=response.service_name
        qaJson["category"]=response.category
        qaJson["question"]=response.question
        qaJson["answer"]=response.answer
        for tag in response.tag:
            tags.append(tag)
        qaJson["tag"]=tags
    print(type(qaJson))
    return json.dumps(qaJson, default=list)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
