pipeline {
    agent any

    environment {
        SONARQUBE_URL = 'http://localhost:9000'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev', url: 'https://github.com/sdeshpande755/sonarqube-demoo.git'
            }
        }

        stage('Run Tests & Generate Coverage') {
            steps {
                sh '''
                    pip install coverage  # Ensure coverage is installed
                    coverage run -m unittest discover
                    coverage xml -o coverage.xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube Scanner'

                    withSonarQubeEnv('SonarQube_server') {
                        withCredentials([string(credentialsId: 'testing', variable: 'SONARQUBE_TOKEN')]) {
                            sh """
                                ${scannerHome}/bin/sonar-scanner \\
                                -Dsonar.projectKey=testing \\
                                -Dsonar.sources=. \\
                                -Dsonar.host.url=${SONARQUBE_URL} \\
                                -Dsonar.login=${SONARQUBE_TOKEN} \\
                                -Dsonar.python.coverage.reportPaths=coverage.xml
                            """
                        }
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 5, unit: 'MINUTES') {
                        def qualityGate = waitForQualityGate()
                        if (qualityGate.status != 'OK') {
                            error "❌ Pipeline failed due to Quality Gate: ${qualityGate.status}"
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed! Check logs & SonarQube for details."
        }
    }
}
