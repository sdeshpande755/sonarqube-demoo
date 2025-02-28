pipeline {
    agent any  

    environment {
        SONARQUBE_URL = 'http://localhost:9000'  
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    def branchName = env.BRANCH_NAME
                    echo "Current branch: ${branchName}"

                    if (branchName == 'dev' || branchName.startsWith('PR-')) {  
                        git branch: 'dev', url: 'https://github.com/sdeshpande755/sonarqube-demoo.git'
                    } else {
                        error "Build aborted: Only 'dev' branch and PRs targeting 'dev' are allowed."
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube Scanner'  
                    withSonarQubeEnv('SonarQube_server') {  
                        withCredentials([string(credentialsId: 'sonar-token', variable: 'SONARQUBE_TOKEN')]) {  
                            sh """
                                ${scannerHome}/bin/sonar-scanner \\
                                -Dsonar.projectKey=Sonar_Token \\
                                -Dsonar.sources=. \\
                                -Dsonar.host.url=${SONARQUBE_URL} \\
                                -Dsonar.login=${SONARQUBE_TOKEN}
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
