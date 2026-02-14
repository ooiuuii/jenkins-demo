pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "代码已拉取"
            }
        }

        stage('Build') {
            steps {
                sh 'echo 开始构建'
                sh 'sleep 2'
            }
        }

        stage('Test') {
            steps {
                sh 'echo 执行测试'
                sh 'sleep 2'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo 模拟部署'
            }
        }
    }
}
