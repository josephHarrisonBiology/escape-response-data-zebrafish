The Zebrafish-Larvae-Escape-Data repository contains a comprehensive dataset of escape response behavior observed in zebrafish larvae. The data has been collected through a series of carefully controlled experiments designed to study various aspects of escape responses. This resource aims to provide valuable information for researchers and students who are interested in understanding the neural mechanisms underlying escape responses in zebrafish larvae, as well as those who wish to conduct meta-analyses or comparative studies.

The dataset includes parameters such as:

Stimulus type: This refers to the nature of the stimuli used to elicit escape responses in the zebrafish larvae. Examples include visual, mechanical, or chemical stimuli.
Response latency: This is the time taken for the zebrafish larvae to initiate an escape response after the stimulus has been applied.
Locomotion patterns: This describes the specific movement patterns displayed by the zebrafish larvae during their escape response, such as C-start or S-start, which are well-known escape behaviors in fish.
In addition, the dataset contains information on various other variables, such as age, size, and genetic background of the zebrafish larvae, which can be useful for researchers interested in studying the influence of these factors on escape response behaviors.

The data is provided in a well-structured and easy-to-use format, such as CSV or Excel, which can be easily imported into various data analysis tools and software.

The linear regression model code provided in this repository is designed to predict the response angle of larval zebrafish using a neural network. The model uses the type of stimulus and collision angle to predict the angle of response. The dataset used to train the model is carefully controlled and includes parameters such as stimulus type, response latency, and locomotion patterns.

The model is defined using a sequential neural network with three dense layers, with the first two layers having 32 and 16 nodes respectively, both with the ReLU activation function. The output layer has a single node and no activation function, as the model is trained to predict a continuous value. The model is compiled with a mean squared error loss function and the Adam optimizer.

The dataset is preprocessed using a simple imputer to handle missing values, and then split into features (stimulus size and collision angle) and target (turn angle) for training. The model is trained on the training data with 100 epochs and a batch size of 16.

After training, the model is used to make a prediction for each turn angle from 1-180 and each stimulus size from 0.1 to 5.0. The predicted angles are logged with the corresponding input data, allowing researchers to analyze the performance of the model and its accuracy in predicting response angles.

Overall, this linear regression model code provides a useful tool for researchers and students interested in studying escape responses in zebrafish larvae and can be used to further advance our understanding of this important behavior.

We encourage researchers and students to contribute to the repository by adding new data, analyses, or resources related to zebrafish larvae escape responses. Collaborations and suggestions for improvement are always welcome, as we strive to make this repository an invaluable tool for advancing our understanding of escape responses in zebrafish larvae and beyond.
