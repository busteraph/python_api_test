#!flask/bin/python
from flask import Flask, jsonify
app = Flask(__name__)


schema = [
    {
        'id': 'ínteger',
        'nom': 'string',
        'prenom': 'string', 
        'date_naissance': 'date'
    }
]

@app.route('/test/api/v1.0/schema', methods=['GET'])
def get_schema():
    return jsonify({'schema': schema})

if __name__ == '__main__':
    app.run(debug=True)