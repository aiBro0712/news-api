from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)
app.config ['MONGO_URI'] = 'mongodb://localhost:27017/myDatabase'
mongo = PyMongo(app)


@app.route('/news/<int:id>', methods=['GET'])
def get_one_news_artical(id):
    a_article =  mongo.db.news_data.find_one_or_404({'_id': id})
    result = dumps(a_article)
    return result


if __name__ == "__main__":
    app.run(debug=True)