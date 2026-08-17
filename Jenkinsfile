pipeline {
    agent any

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
                sh 'python3 -m venv venv && venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh '~/.local/bin/pytest --alluredir=allure-results -v || true'
            }
        }
    }


    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
