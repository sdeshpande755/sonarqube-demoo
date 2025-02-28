pipeline {
    agent any  // Runs on any available agent

    environment {
        SONARQUBE_URL = 'http://localhost:9000'  // Update if needed
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev', url: 'https://github.com/sdeshpande755/sonarqube-demoo.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube Scanner'  // Ensure this is configured in Jenkins

                    withSonarQubeEnv('SonarQube_server') {  // Change this to match your Jenkins SonarQube config
                        withCredentials([string(credentialsId: 'sonar-token', variable: 'SONARQUBE_TOKEN')]) {  // Update with correct credentials ID
                            sh """
                                ${scannerHome}/bin/sonar-scanner \\
                                -Dsonar.projectKey=Sonar_Token \\
                                -Dsonar.sources=. \\
                                -Dsonar.host.url=${SONARQUBE_URL} \\
                                -Dsonar.login=${SONARQUBE_TOKEN}
                                -Dsonar.branch.name=dev
                            """
                        }
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}


