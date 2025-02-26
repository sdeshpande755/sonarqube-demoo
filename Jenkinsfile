pipeline {
    agent any

    environment {
        SONARQUBE_URL = 'http://localhost:9000'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature/sonarqube-setup', url: 'https://github.com/sdeshpande755/sonarqube-demoo.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube Scanner'  // Ensure it's configured in Jenkins

                    withSonarQubeEnv('SonarQube') {  // Ensure this matches Jenkins' SonarQube config
                        withCredentials([string(credentialsId: 'sqp_3552fa2fbc844a05199a16e45a6b0ce8fbb42e20', variable: 'SONARQUBE_TOKEN')]) {
                            sh """
                                ${scannerHome}/bin/sonar-scanner \
                                -Dsonar.projectKey=python-sonarqube \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=${SONARQUBE_URL} \
                                -Dsonar.login=${SONARQUBE_TOKEN}
                            """
                        }
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}