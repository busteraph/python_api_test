#!flask/bin/python
from flask import Flask, jsonify
app = Flask(__name__)


schema = [
    # {
    #     'id': 'ínteger',
    #     'nom': 'string',
    #     'prenom': 'string', 
    #     'date_naissance': 'date'
    # }
]

@app.route('/test/api/v1.0/schema', methods=['GET'])
def get_schema():
    return jsonify({'schema': schema})

from flask import request
@app.route('/test/api/v1.0/schema', methods=['POST'])
def create_schema():
    if not request.json or not 'id' in request.json:
        abort(400)
    sc = {
        'id': request.json['id'],
        'nom': request.json['nom'],
        'prenom': request.json.get('prenom', ""),
        'date_naissance': request.json['date_naissance']
    }
    schema.append(sc)
    return jsonify({'schema': schema}), 201

if __name__ == '__main__':
    app.run(debug=True)