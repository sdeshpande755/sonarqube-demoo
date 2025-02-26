pipeline {
    agent any

    environment {
        SONARQUBE = 'SonarQubeServer'  // Ensure this is correctly set up in Jenkins
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'feature/sonarqube-setup', url: 'https://github.com/sdeshpande755/sonarqube-demoo.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQubeServer') {
                        sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=sonarqube-Demoo \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://localhost:9000 \
                          -Dsonar.login=sqp_3a2c0eb1ab3f36d4d1ff6811cbf5e27575c54d07
                        '''
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 1, unit: 'MINUTES') {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline failed due to quality gate failure: ${qg.status}"
                        }
                    }
                }
            }
        }
    }

    post {
        failure {
            echo "Build failed. Check SonarQube report."
        }
    }
}