
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\gopar\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\gopar\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t event-registration:1.0 .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s\\deployment.yaml'
                bat 'kubectl rollout status deployment/event-registration --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
