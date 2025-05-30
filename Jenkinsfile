pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sharan-sant/iot-hvac'
        DOCKER_CREDENTIALS_ID = 'jenkins'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Injecting MQTT credentials..."
                withCredentials([
                    file(credentialsId: 'MQTT_KEY', variable: 'MQTT_KEY_PATH'),
                    file(credentialsId: 'MQTT_CRT', variable: 'MQTT_CRT_PATH')
                ]) {
                    sh '''
                        cp "$MQTT_KEY_PATH" ./mqtt.key
                        cp "$MQTT_CRT_PATH" ./mqtt.crt
                        docker build -t $IMAGE_NAME .
                    '''
                }
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into DockerHub..."
                withCredentials([usernamePassword(credentialsId: "$DOCKER_CREDENTIALS_ID", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing image to DockerHub..."
                sh 'docker push $IMAGE_NAME'
            }
        }
    }
}
