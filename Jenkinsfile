pipeline {

    agent any

    environment {

        DOCKER_USER = 'zaibjahan200'
    }

    stages {

        stage('Fetch') {

            steps {

                checkout scm

            }
        }

        stage('Build and Run') {

            steps {

                sh '''
                docker build -t sentiment-api:test .
                docker rm -f sentiment-test || true

                docker run -d \
                --name sentiment-test \
                -p 5000:5000 \
                sentiment-api:test
                '''
            }
        }

        stage('Unit Test') {

            steps {

                
                sh 'docker exec sentiment-test pytest tests/test_api.py'
            }
        }

        stage('UI Test') {

            steps {

                sh 'docker exec sentiment-test pytest tests/test_ui.py'
            }
        }

        stage('Build and Push') {

            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {

                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin

                    docker build \
                    -t zaibjahan200/sentiment-api:unstable .

                    docker push \
                    zaibjahan200/sentiment-api:unstable
                    '''
                }
            }
        }

        stage('Deploy to Minikube') {

            steps {

                sh '''
                kubectl apply -f k8s/pvc.yaml

                kubectl apply -f k8s/blue-deployment.yaml

                kubectl apply -f k8s/green-deployment.yaml

                kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }
}
