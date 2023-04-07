import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Load the CSV data into a pandas DataFrame
data = pd.read_csv('/Users/joe/Documents/test.csv')

# Preprocess the data to handle missing values
imputer = SimpleImputer(strategy='mean')
data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Split the data into features (X) and target (y)
X = data[['STIMULUS SIZE', 'COLLISION ANGLE']]
y = data['TURN ANGLE']

# Define the range of stimulus sizes and angles to loop through
stimulus_sizes = np.arange(0.1, 5.1, 0.1)
collision_angles = np.arange(1, 181)

# Define the neural network model
model = Sequential()
model.add(Dense(32, input_dim=2, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model on the training data
model.fit(X, y, epochs=100, batch_size=16, verbose=0)

# Make a prediction for each turn angle from 1-180 and each stimulus size from 0.1 to 5.0
predicted_angles = []
for stimulus_size in stimulus_sizes:
    for collision_angle in collision_angles:
        new_input = np.array([[stimulus_size, collision_angle]])
        predicted_angle = model.predict(new_input)
        predicted_angles.append(predicted_angle[0][0])
        
        # Log the predicted angle with the input data
        print(f"Predicted turn angle: {predicted_angle[0][0]:.2f} With Input Data: Stimulus Size: {stimulus_size}, collision angle: {collision_angle}")
