from flask import Flask, request, jsonify


app = Flask(__name__)

rides = [
    {
        'id': 1,
        'Name': 'Nairobi',
        'Departure_to_Destination': '3:10_to_Coast',
        'status': 'Not taken'
    },
    {
        'id': 2,
        'Name': 'Malindi',
        'Departure_to_Destination': '6:30_to_Nairobi',
        'status': 'Taken'
    }
]


@app.route('/ride/api/v1/rides', methods=['POST'])
def create_ride():
    "Driver creates a ride for viewing"

    #Convert ride details from driver into a description
    time = str(request.json['time'])
    destination = str(request.json['destination'])
    details = time + ' ' + 'to' + ' ' destination

    ride = {
        'id': len(rides) + 1,
        'Name': request.json['Name'],
        'description': details,
        'status': 'Not taken'
    }

    rides.append(ride)
    return jsonify({'ride': ride}), 201

if __name__ == '__main__':
    app.run(debug=True)
