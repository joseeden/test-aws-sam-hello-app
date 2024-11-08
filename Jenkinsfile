pipeline {

    agent any
    environment {
        AWS_SAM_STACK_NAME = 'sam-app' 
        AWS_DEFAULT_REGION = 'ap-southeast-1'
        AWS_ACCESS_KEY_ID = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')        
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    // Create and activate virtual environment
                    sh "python3 -m venv venv"
                    sh ". venv/bin/activate && pip install -r tests/requirements.txt"
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh ". venv/bin/activate && pytest"
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build SAM app
                    sh ". venv/bin/activate && sam build -t template.yaml"
                }
            }
        }

        stage('Deploy') {
            
            steps {
                script {
                    // Deploy SAM app
                    sh ". venv/bin/activate && sam deploy -t template.yaml --no-confirm-changeset --no-fail-on-empty-changeset --region ${AWS_DEFAULT_REGION}"
                }
            }
        }
    }
}
