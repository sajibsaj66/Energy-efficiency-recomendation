from flask import Flask, request, jsonify
from flask_cors import CORS
from recomendation import energy_efficiency_recommendations

app = Flask(__name__)
CORS(app)


@app.route("/energy_recomendation", methods=["POST"])
def enery_recomendation():

    data = request.json

    property_data = {
        'Property Type': ['House'],
        'Location': ['Urban'],
        'Square Footage': [1800],
        'Number of Bedrooms': [4],
        'Number of Bathrooms': [2],
        'Roof Type': ['Asphalt'],
        'Year of Construction': [2005],
        'Primary Energy Source': ['Gas'],
        'Number of Occupants': [4],
        'Heating System': ['Gas'],
        'Cooling System': ['Central AC'],
        'Water Heating System': ['Tankless'],
        'Thermostat Type': ['Smart'],
        'Lighting Type': ['LED'],
        'Roof Insulation': ['Fiberglass'],
        'Wall Insulation': ['Foam'],
        'Major Appliances': ['Refrigerator, Dishwasher'],
        'Window Type': ['Double Pane'],
        'Door Type': ['Fiberglass'],
        'Solar Panel': ['No'],
        'Other Renewable Energy Source': ['No']
    }

    recomendation = energy_efficiency_recommendations(
        property_data)

    return jsonify({"response": recomendation}), 200


if __name__ == "__main__":
    app.run(debug=True)
