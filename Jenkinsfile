pipeline {
  agent any

  stages {
    stage('Test') {
      steps {
        sh '''
          docker run --rm \
            --network ci \
            --volumes-from jenkins \
            -w /var/jenkins_home/workspace/demo-pipeline \
            python:3.11-slim bash -lc "
              pip install -U pip &&
              pip install -r requirements.txt &&
              pytest -v --html=report.html --self-contained-html
            "
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'report.html', fingerprint: true
    }
  }
}
