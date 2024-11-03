pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    sh "python3 -m venv venv"
                    sh ". venv/bin/activate && pip install -r tests/requirements.txt"
                }
            }
        }
        
        stage('Test') {
            environment {
                AWS_SAM_STACK_NAME = 'AWS SAM App' 
            }
            steps {
                script {
                    sh ". venv/bin/activate && pytest"
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh ". venv/bin/activate && sam build -t template.yaml"
                }
            }
        }

        stage('Deploy') {
            environment {
                AWS_DEFAULT_REGION = 'ap-southeast-1'
                AWS_ACCESS_KEY_ID = credentials('aws-access-key')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
            }
            steps {
                script {
                    sh ". venv/bin/activate && sam deploy -t template.yaml --no-confirm-changeset --no-fail-on-empty-changeset"
                }
            }
        }
    }
}
