
# Kidney Tumor Detection Using Deep Learning

This project implements an end-to-end machine learning pipeline for identifying kidney tumors from CT scan images. It leverages a pretrained VGG16 model with a custom fully connected layer for tumor classification. The project includes data ingestion, model training, evaluation, and deployment workflows, all managed with MLOps principles.

##  Features:
- **Dataset**: kidney CT scan images (Tumor/Normal).
    - dataset link :- https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone 
- **Model**: Transfer learning with VGG16 (Imagenet weights) and custom classifier layers.
- **Data Augmentation**: Enhances dataset for better generalization.
- **MLOps Integration**:
    - Config-driven pipeline setup with YAML.
    - Data versioning and workflow tracking using DVC.
    - Modular project structure with reusable components.
- **Deployment**: Dockerized Flask app for serving the model and deployed on AWS.
- **Utilities**: Common functions for reading YAML, saving JSON, and handling data.
- **Project Workflow**:
    - Data ingestion and preprocessing.
    - Model training and evaluation.
    - Deployment with Docker and AWS.

# How to run?


### STEPS:
Clone the repository
```bash
https://github.com/Immortal-Pi/TumorFlow
```

### STEP 01- Create a conda environment after opening the repository
```bash 
conda create -n mlopscnn python=3.9 -y
```
```bash 
conda activate mlopscnn
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

# Finally run the following command
```bash
python app.py
```

Now,

open up you local host and port

# MLflow & pipeline tracking

dagshub repo : https://dagshub.com/Immortal-Pi/TumorFlow 

```bash
import dagshub
dagshub.init(repo_owner='your-github-username', repo_name='your-repository-name', mlflow=True)
```

### DVC commands

    1. dvc init 
    2. dvc repro
    3. dvc dag 

### Data-pipeline 

![Data Pipeline](https://github.com/Immortal-Pi/TumorFlow/blob/main/documentation/datapipeline3.png) 

### mlflow Integration

![MLFlow Dashboard](https://github.com/Immortal-Pi/TumorFlow/blob/main/documentation/mlflow1.png)

![MLFlow Experiment](https://github.com/Immortal-Pi/TumorFlow/blob/main/documentation/mlflow2.png)

## AWS CICD Deployment with Github Actions

    1. Login to AWS console 
    2. Create IAM use for deployment 

```bash
# with specific access
    1. ECR access
    2. ECR Elastic Container 

# Description: About the deployment 
    1. Build docker image of the source code 
    2. Push the docker imange to ECR
    3. Launch your EC2 
    4. Pull your image from ECR in EC2 
    5. Launch your docker image in EC2 

# Policy 
    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess
```

## 3. Create ECR repo to store/save docker image 
    - save the URI: 011528265658.dkr.ecr.us-east-2.amazonaws.com/kidney (example)

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and install docker in EC2 Machine 
```bash
# installation of docker on the virtual machine
    sudo apt-get update -y
    sudo apt-get upgrade
    #required
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
```

## Demo 

![UI Demo](https://github.com/Immortal-Pi/TumorFlow/blob/main/documentation/UI.gif)

## Tech Stack 

- **Programming Language**: Python
- **Deep Learning Framework**: Keras with TensorFlow backend
- **MLOps Tools**:
    - DVC (Data Version Control) for pipeline tracking and data versioning
    - Docker for containerization
- **Web Framework**: Flask for model deployment
- **Cloud Platform**: AWS for hosting the model
- **Version Control**: Git and GitHub
- **Data Utilities**: YAML, JSON handling, and custom preprocessing functions
- **Base Model**: VGG16 (pretrained on ImageNet)

## Conclusion
This project highlights the integration of MLOps principles in managing the entire machine learning lifecycle. While the focus was on building a kidney tumor detection model using transfer learning, the core objective was to emphasize the importance of project structure, automation of workflows, and the use of MLOps tools like DVC for version control and Docker for deployment. It serves as a foundation for understanding how to design scalable, maintainable, and efficient ML pipelines, ensuring reproducibility and streamlined collaboration in real-world scenarios.
