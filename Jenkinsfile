pipeline {
    agent any

    environment {
        SONARQUBE = 'SonarQubeServer'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'feature/sonarqube-setup', url: https://github.com/sdeshpande755/sonarqube-demoo.git
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQubeServer') {
                        sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=sonarqube-demo \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://localhost:9000 \
                          -Dsonar.login=sqp_2691f027ea2f89f15bcfccf11ff8c942bd7d2d13
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