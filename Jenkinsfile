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
                sh 'python3 -m pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Install Playwright') {
            steps {
                sh 'PLAYWRIGHT_BROWSERS_PATH=/var/lib/jenkins/.cache/ms-playwright venv/bin/playwright install chromium'
            }
        }

        stage('Run tests') {
            steps {
                sh 'PLAYWRIGHT_BROWSERS_PATH=/var/lib/jenkins/.cache/ms-playwright python3 -m pytest --alluredir=allure-results -v || true'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
        }
    }
}
