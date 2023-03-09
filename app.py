from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import spacy

app = Flask(__name__)
api = Api(app)


class Similarity(Resource):
    def post(self):
        
        posted_data = request.get_json()

        text1 = posted_data["text1"]
        text2 = posted_data["text2"]

        nlp = spacy.load("en_core_web_sm")

        text1 = nlp(text1)
        text2 = nlp(text2)

        ratio = text1.similarity(text2)

        retJson = {
            "Statuc Code": 200,
            "Similarity Ratio": ratio
        }

        return jsonify(retJson)

api.add_resource(Similarity, "/similarity")

if __name__ == "__main__":
    app.run(host="0.0.0.0")