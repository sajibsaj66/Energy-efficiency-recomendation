import pandas as pd
import random

# Create an empty DataFrame with columns
columns = [
    'Property Type',
    'Location',
    'Square Footage',
    'Number of Bedrooms',
    'Number of Bathrooms',
    'Roof Type',
    'Year of Construction',
    'Current Monthly Energy Usage',
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

# Create 100 rows of dummy data
data = []
for _ in range(100):
    row = [
        random.choice(['House', 'Apartment', 'Condo']),
        random.choice(['Urban', 'Suburban', 'Rural']),
        random.randint(1000, 5000),
        random.randint(1, 5),
        random.randint(1, 4),
        random.choice(['Asphalt', 'Metal', 'Tile', 'Other']),
        random.randint(1980, 2023),
        random.uniform(50, 300),
        random.choice(['Electric', 'Gas', 'Solar', 'Other']),
        random.randint(1, 10),
        random.choice(['Forced Air', 'Radiant', 'Heat Pump', 'Gas', 'Other']),
        random.choice(['Central AC', 'Window AC', 'None']),
        random.choice(['Tankless', 'Storage', 'Heat Pump', 'Other']),
        random.choice(['Smart', 'Programmable', 'Manual']),
        random.choice(['Incandescent', 'CFL', 'LED']),
        random.choice(['Fiberglass', 'Foam', 'Other']),
        random.choice(['Fiberglass', 'Foam', 'Other']),
        ', '.join(random.sample(['Refrigerator', 'Dishwasher', 'Washer',
                  'Dryer', 'Oven', 'Microwave', 'Other'], random.randint(2, 7))),
        random.choice(['Single Pane', 'Double Pane', 'Low-E']),
        random.choice(['Wood', 'Metal', 'Fiberglass']),
        random.choice(['Yes', 'No']),
        random.choice(['Yes', 'No'])
    ]
    data.append(row)

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('dummy_energy_data.csv', index=False)
