pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test Flask Application') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Flask application test passed!'
        }
        failure {
            echo 'FAILURE: Flask application test failed!'
        }
    }
}