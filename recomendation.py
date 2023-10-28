import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import warnings

warnings.filterwarnings("ignore")

# Load your dataset (replace 'your_dataset.csv' with your actual data file).
data = pd.read_csv('./data/dummy_energy_data.csv')
data.head()

# Define the features and the target variable
features = [
    'Property Type',
    'Location',
    'Square Footage',
    'Number of Bedrooms',
    'Number of Bathrooms',
    'Roof Type',
    'Year of Construction',
    'Primary Energy Source',
    'Number of Occupants',
    'Heating System',
    'Cooling System',
    'Water Heating System',
    'Thermostat Type',
    'Lighting Type',
    'Roof Insulation',
    'Wall Insulation',
    'Major Appliances',
    'Window Type',
    'Door Type',
    'Solar Panel',
    'Other Renewable Energy Source'
]

# Use this column as the target variable
target = 'Current Monthly Energy Usage'

# Preprocess the data
# Remove rows with missing data (you can choose to handle missing data differently)
data = data.dropna()

# Convert categorical variables to dummy variables
data = pd.get_dummies(data, columns=features, drop_first=True)

# Split the data into training and testing sets
X = data.drop(target, axis=1)
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train a machine learning model (Random Forest in this example)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Squared Error: {mse:.2f}')
print(f'Mean Absolute Error: {mae:.2f}')

# Provide energy efficiency upgrade recommendations based on the predictions


def energy_efficiency_recommendations(property_data):
    # Convert categorical variables to dummy variables for the input data
    property_data = pd.get_dummies(
        property_data, columns=features, drop_first=True)

    # Use the trained model to predict current monthly energy usage
    predicted_energy_usage = model.predict([property_data])[0]
    print(f"---------------{predicted_energy_usage}-------------")

    # # Get feature importances
    # feature_importance = model.feature_importances_

    # # Sort features by importance
    # important_features = [features[i] for i in range(
    #     len(features)) if feature_importance[i] > 0.05]

    # # Create a dictionary to store upgrade recommendations for each feature
    # upgrade_recommendations = {}

    # for feature_name in important_features:
    #     # You can customize this section to provide specific upgrade recommendations for each feature.
    #     # For example, if the feature is 'Roof Insulation':
    #     if 'Roof Insulation' in feature_name:
    #         upgrade_recommendations[feature_name] = "Upgrade roof insulation to a more energy-efficient material."
    #     elif 'Heating System' in feature_name:
    #         upgrade_recommendations[feature_name] = "Consider upgrading the heating system to a more efficient option."
    #     # Add more specific upgrade suggestions for other features as needed

    # return upgrade_recommendations
    return predicted_energy_usage


# # Example property data (customize this with your actual data)
# property_data = {
#     'Property Type': ['House'],  # Adjust the values based on your dataset
#     'Location': ['Urban'],
#     'Square Footage': [1800],
#     'Number of Bedrooms': [4],
#     'Number of Bathrooms': [2],
#     'Roof Type': ['Asphalt'],
#     'Year of Construction': [2005],
#     'Primary Energy Source': ['Gas'],
#     'Number of Occupants': [4],
#     'Heating System': ['Gas'],
#     'Cooling System': ['Central AC'],
#     'Water Heating System': ['Tankless'],
#     'Thermostat Type': ['Smart'],
#     'Lighting Type': ['LED'],
#     'Roof Insulation': ['Fiberglass'],
#     'Wall Insulation': ['Foam'],
#     'Major Appliances': ['Refrigerator, Dishwasher'],
#     'Window Type': ['Double Pane'],
#     'Door Type': ['Fiberglass'],
#     'Solar Panel': ['No'],
#     'Other Renewable Energy Source': ['No']
# }

# # Get energy efficiency upgrade recommendations for the example property data
# upgrade_recommendations = energy_efficiency_recommendations(
#     property_data)
# for feature, recommendation in upgrade_recommendations.items():
#     print(f"Upgrade {feature}: {recommendation}")
