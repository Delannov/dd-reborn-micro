pipeline {
    agent any
    stages {

        stage('Sanity check') {
            steps {
                input "Testing input?"
            }
        }

        stage('stage') {
            steps {
                sh './testing'
            }
        }

    }
}
