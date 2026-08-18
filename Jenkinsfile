pipeline {
    agent { docker { image 'mcr.microsoft.com/playwright/python:v1.62.0-noble'; args '-u root' } }

    environment {
        ALLURE_RESULTS = 'allure-results'
        CI = 'true'
        DB_HOST = credentials('DB_HOST')
        DB_PORT = credentials('DB_PORT')
        DB_NAME = credentials('DB_NAME')
        DB_USER = credentials('DB_USER')
        DB_PASS = credentials('DB_PASS')
    }

    triggers {
        cron('H 3 * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'npm install -g allure'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest --alluredir=allure-results -v || true'
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate allure-results --clean -o allure-report'
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
        }
    }
}
