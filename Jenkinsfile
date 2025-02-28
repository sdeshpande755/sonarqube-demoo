pipeline {
    agent any  // Runs on any available agent

    environment {
        SONARQUBE_URL = 'http://localhost:9000'  // Update if needed
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    try {
                        git branch: 'invalid_branch', url: 'https://github.com/sdeshpande755/sonarqube-demoo.git'
                    } catch (Exception e) {
                        error "Checkout failed: ${e.message}"
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    try {
                        def scannerHome = tool 'SonarQube Scanner'  // Ensure this is configured in Jenkins

                        withSonarQubeEnv('SonarQube_server') {  // Change this to match your Jenkins SonarQube config
                            withCredentials([string(credentialsId: 'testing', variable: 'SONARQUBE_TOKEN')]) {  // Update with correct credentials ID
                                sh """
                                    ${scannerHome}/bin/sonar-scanner \\
                                    -Dsonar.projectKey=testing \\
                                    -Dsonar.sources=. \\
                                    -Dsonar.host.url=${SONARQUBE_URL} \\
                                    -Dsonar.login=${SONARQUBE_TOKEN}
                                """
                            }
                        }
                    } catch (Exception e) {
                        error "SonarQube analysis failed: ${e.message}"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    try {
                        timeout(time: 5, unit: 'MINUTES') {
                            def qualityGate = waitForQualityGate()
                            if (qualityGate.status != 'OK') {
                                error "Pipeline failed due to Quality Gate: ${qualityGate.status}"
                            }
                        }
                    } catch (Exception e) {
                        error "Quality Gate check failed: ${e.message}"
                    }
                }
            }
        }
    }
}

