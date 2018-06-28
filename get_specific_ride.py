from flask import Flask, jsonify
from flask import abort, make_response, render_template
from create_ride import rides    #Get a list of created rides


app = Flask(__name__)

@app.route('/ride/api/v1/rides/<int:ride_id>', methods=['GET'])
def get_specific_ride(ride_id):
    "A user gets the specific details of a ride"
    ride = [ride for ride in rides if ride['id'] == ride_id]

    if len(ride) == 0:
        print('Ride not found')
        '''@app.errorhandler(404)
        def not_found(error):
            return make_response(jsonify({'error': 'Not found'}), 404)
            return render_template('404.html'), 404'''
    return jsonify({'ride': ride[0]})



if __name__ == '__main__':
    app.run(debug=True)
