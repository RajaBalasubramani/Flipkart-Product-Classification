# Flipkart-Product-Classification

This project focuses on scraping various categories of product images from Flipkart and training a Convolutional Neural Network (CNN) model to classify the products based on the input image.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Prediction](#prediction)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
In this project, we aim to automatically classify products based on their images using deep learning techniques. We scrape product images from Flipkart, preprocess the data, train a CNN model, and evaluate its performance. Finally, we provide an interface for predicting the product category using a trained model.

## Installation
1. Clone the repository: https://github.com/Raja27112002/Flipkart-Product-Classification.git

2. Install the required dependencies: pip install -r requirements.txt


## Usage
1. Run the data scraping script to collect the product images: Scrapper.py
( Change the number in range() function to download more number of images from more pages)

2. Use the Jupyter file to preprocess,train and test a CNN Model



## Dataset
The dataset used in this project consists of product images collected from Flipkart. The images are organized into different categories, such as electronics, clothing, home appliances, etc.

## Model Training
For training the model, we employ a CNN architecture using TensorFlow and Keras. The model is trained on the preprocessed dataset with a specified number of epochs.

## Model Evaluation
To evaluate the model's performance, we calculate various metrics such as accuracy, precision, and recall. We also generate a confusion matrix to assess the model's ability to correctly classify different product categories.

## Prediction
Once the model is trained, you can use it to predict the product category of a given input image. The `predict_product.py` script takes an input image and outputs the predicted product category.

## Contributing
Contributions to this project are always welcome. If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).



