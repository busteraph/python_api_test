#!flask/bin/python
from flask import Flask, jsonify
app = Flask(__name__)


# curl -i -H "Content-Type: application/json" -X POST -d '{"id":"integer", "nom":"string", "prenom":"string", "date_naissance":"date"}' http://localhost:5000/test/api/v1.0/schema

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

# curl -i -H "Content-Type: application/json" -X POST -d '{"nom":"Personne", "prenom":"Inconnue", "date_naissance":"9999-12-31"}' http://localhost:5000/test/api/v1.0/upload_dataset
@app.route('/test/api/v1.0/upload_dataset', methods=['POST'])
def upload_dataset():
    if not request.json:
        abort(400)

    dataset = {
        'nom': request.json['nom'],
        'prenom': request.json.get('prenom', ""),
        'date_naissance': request.json['date_naissance']
    }
    return jsonify({'dataset': dataset}), 201


from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)