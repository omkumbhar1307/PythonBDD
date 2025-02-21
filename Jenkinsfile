pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python test_runner.py'
            }
        }

        stage('Publish Report') {
            steps {
                junit 'reports/*.xml'  // If using JUnit-style reports
            }
        }
    }
}
