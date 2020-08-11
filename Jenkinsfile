pipeline {
    agent any
    stages {

        stage('Sanity check') {
            steps {
                input "WARNING THIS IS PRODUCTION PIPELINE! Do you want to proceed?"
            }
        }

        stage('stage') {
            steps {
                sh './testing'
            }
        }

    }
}
