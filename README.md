## Potato Leaf Disease Classification

The goal of this research is to create a convolutional neural network (CNN) that can categorize illnesses of potato leaves. Accurately determining if a potato leaf is healthy, blight-affected early or late is the aim. It consists of a web application for real-time leaf classification and a TensorFlow model trained on the potato leaf disease dataset.

### Project Components

#### Convolutional Neural Network (CNN)

TensorFlow is used in a Jupyter Notebook inside of VSCode to build the CNN model. It learns and divides potato leaf photos into three groups: healthy, early blight, and late blight. It does this by utilizing deep learning algorithms. The notebook contains specifics on the model's construction and training procedure.

#### Web Application

To input photos of potato leaves and get predictions from the trained CNN model, use the web application's intuitive interface. It shows the probability score for each class as well as the expected class (healthy, early blight, or late blight). With this application, users may evaluate the health of potato plants rapidly.

#### Deployment on Google Cloud

For scalability and accessibility, the trained TensorFlow CNN model is hosted on Google Cloud Platform (GCP). Its smooth interaction with the online application is made possible by its storage in a cloud storage bucket. The deployment procedure makes sure that cloud resources are used effectively for jobs involving inference and prediction.

#### API Server

To enable communication between the web application and the TensorFlow model that is installed on GCP, an API server is put into place. This server receives incoming picture requests, runs the CNN model on them, and instantly provides the web application with the classified images. It guarantees the leaf classification system's dependability and seamless operation.

### Technologies Used
- Python
- TensorFlow
- Jupyter Notebook in VS Code
- Fastapi
- HTML/CSS/JavaScript
- Google Cloud Storage
- Google Cloud Platform (GCP)