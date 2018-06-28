from flask import Flask, jsonify
from create_ride import rides    #Get a list of created rides


app = Flask(__name__)

@app.route('/ride/api/v1/rides', methods=['GET'])
def get_rides():
    "A user gets all available ride offers"
    return jsonify({'rides': rides})


if __name__ == '__main__':
    app.run(debug=True)
