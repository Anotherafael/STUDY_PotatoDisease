## Potato Leaf Disease Classification

This project uses a Convolutional Neural Network (CNN) model constructed with TensorFlow to categorise illnesses of the potato leaf. The [Plant Village](https://www.kaggle.com/datasets/arjuntejaswi/plant-village) dataset on Kaggle was used to train and test the model, which can differentiate between healthy and diseased potato leaves. The CNN is optimised for image classification using the proper loss functions and optimizers thanks to preprocessing, which also guarantees adequate training and testing sets.

A real-time prediction backend utilising the trained TensorFlow model is offered by FastAPI. Endpoints manage the uploading of images and provide categorization results, while Uvicorn effectively manages the FastAPI programme. TensorFlow Serving and the FastAPI backend are created in distinct containers by Docker, which containerises the services. Docker Compose is used to manage the network and facilitate seamless communication.

The ReactJS front-end application provides an easy-to-use interface for classifying diseases, enabling users to upload photos and examine the results. Along with being containerised and deployed with the backend services, this frontend communicates with the FastAPI backend to make predictions.

<center>

![Web demonstration](assets/potato-disease-home-page.gif "Web demonstration")

</center>

### Technologies Used

- **Python:** For backend development and machine learning model.
- **TensorFlow:** For building and training the CNN model.
- **TensorFlow Serving:** For serving the trained model.
- **FastAPI:** For creating the backend API.
- **Uvicorn:** ASGI server for the FastAPI application.
- **Docker:** For containerizing the services.
- **ReactJS:** For building the frontend application.