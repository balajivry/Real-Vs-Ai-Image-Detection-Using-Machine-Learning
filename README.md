# Real Vs Ai Image Detection Using Machine Learning

## Overview
A web application to detect whether an image is AI-generated or Real Image using Machine Learning. This project features an intuitive web interface built with Flask, allowing users to upload an image and receive a prediction. The application structure includes app.py for the Flask app,in the main folder create a sub folder templates for web page home.html , and a static directory for uploaded images. To get started, install requirements, ensure the static and templates directories exist, and place home.html in templates. Run the Flask app locally with python app.py and access the web interface at http://127.0.0.1:5000/. Make sure to rename the images by using the image renaming script, place all the files and folders in one main folder.

### Dataset

You can find the dataset we used for this project on Kaggle: [Fake AI-generated and Real Image Dataset](https://www.kaggle.com/code/deadlysmile/ai-vs-real-art-detection).

## Project Structure

The project consists of the following main components:
- `app.py/`: Here, you can find the overall application code to start with
- `code.ipynb`: A Jupyter Notebook explaining the model training process.
- `model.hdf5`: The file model.hdf5 contains a saved version of the trained model, which prevents the need to retrain the model each time it is tested.
- `home.html`: The file home.html consists of combined html and css scripts for the web site.

## Directory Structure
	   ## Main folder
    |-- Ai Art Data                             # Folder for AI-generated art data
    |-- Real Art                                # Folder for real art data
    |-- Templates Folder------> home.html       # Folder for HTML templates keep home.html in templates folder
    |-- Static Folder                           # Folder for static files and uploaded images
    |-- app.py                                  # Main application file
    |-- model.hdf5                              # HDF5 file for the trained model
    |-- code.ipynb                              # Jupyter Notebook for model training


## Model Development

I have used a Convolutional Neural Network (CNN) for image classification. The model was trained on a labeled dataset containing both AI-generated and Real images. 
