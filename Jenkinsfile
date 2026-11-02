// Optional: Linux agent with Python 3, Bash, Docker CLI and daemon access.
// Docker access is privileged: use a dedicated learning agent, never an untrusted shared agent.
pipeline {
    agent any
    options { timeout(time: 15, unit: 'MINUTES'); disableConcurrentBuilds() }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
                sh 'bash -n scripts/*.sh'
            }
        }
        stage('Build') { steps { sh 'docker build -t devops-first-pipeline:jenkins-${BUILD_NUMBER} .' } }
        stage('Verify') {
            steps { sh 'bash scripts/container-check.sh devops-first-pipeline:jenkins-${BUILD_NUMBER}' }
        }
    }
    post {
        always { sh 'docker image rm devops-first-pipeline:jenkins-${BUILD_NUMBER} || true' }
    }
}
