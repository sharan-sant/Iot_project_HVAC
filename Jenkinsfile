pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sharan-sant/iot-hvac'
        DOCKER_CREDENTIALS_ID = 'jenkins'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
    }
}
