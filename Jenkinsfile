pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/PRI0005/banking.git'
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    sh 'python -m unittest discover'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'python app.py'
                }
            }
        }
    }
}
