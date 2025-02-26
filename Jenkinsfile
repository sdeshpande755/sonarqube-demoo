pipeline {
    agent any

    environment {
        SONARQUBE_URL = 'http://localhost:9000'  // Change if hosted elsewhere
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
                    def scannerHome = tool name: 'SonarQube Scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'

                    withSonarQubeEnv('SonarQube') {  // Ensure this matches Jenkins SonarQube config
                        withCredentials([string(credentialsId: 'sqp_75b608ef143e3c1a877cc35877bf7a938585f5cb', variable: 'SONARQUBE_TOKEN')]) {
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