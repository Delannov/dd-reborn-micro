pipeline {
    agent any
    stages {
        stage('stage') {
            steps {
                sh './testing'
            }
        }
        stage('deploy') {
            steps {
                sh './deploy'
            }
        }
    }
}
