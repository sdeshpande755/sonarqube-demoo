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
                        // Deliberately using an incorrect repo URL to cause failure
                        git branch: 'dev', url: 'https://github.com/sdeshpande755/non-existent-repo.git'
                        echo "Checkout successful!"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error "Checkout failed: ${e.message}"
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    try {
                        def scannerHome = tool 'SonarQube Scanner'

                        withSonarQubeEnv('SonarQube_server') {
                            withCredentials([string(credentialsId: 'testing', variable: 'SONARQUBE_TOKEN')]) {
                                sh """
                                    ${scannerHome}/bin/sonar-scanner \\
                                    -Dsonar.projectKey=testing \\
                                    -Dsonar.sources=. \\
                                    -Dsonar.host.url=${SONARQUBE_URL} \\
                                    -Dsonar.login=${SONARQUBE_TOKEN}
                                """
                            }
                        }
                        echo "SonarQube analysis completed successfully!"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error "SonarQube analysis failed: ${e.message}"
                    }
                }
            }
        }

        stage('Quality Gate') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    try {
                        timeout(time: 5, unit: 'MINUTES') {
                            def qualityGate = waitForQualityGate()
                            if (qualityGate.status != 'OK') {
                                currentBuild.result = 'FAILURE'
                                error "Pipeline failed due to Quality Gate: ${qualityGate.status}"
                            }
                        }
                        echo "Quality Gate passed successfully!"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error "Quality Gate check failed: ${e.message}"
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline execution completed successfully!"
        }
        failure {
            echo "❌ Pipeline execution failed! Check logs for details."
        }
    }
}
