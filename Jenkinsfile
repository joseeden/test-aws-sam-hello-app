pipeline {
    agent any

    stages {
        stage('Setup') {
            environment {
                AWS_DEFAULT_REGION = 'ap-southeast-1'
                AWS_ACCESS_KEY_ID = credentials('aws-access-key')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
                AWS_SAM_STACK_NAME = 'AWS SAM App'
            }
            steps {
                sh "pip3 install -r tests/requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "pytest"
            }
        }
        stage('Build') {
            steps {
                sh "sam build -t template.yaml"
            }
        }
        stage('Deploy') {
            steps {
                sh "sam deploy -t template.yaml --no-confirm-changeset --no-fail-on-empty-changeset"
            }
        }
    }
}
