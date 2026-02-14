pipeline {
  agent any

  stages {
    stage('Test') {
      steps {
        sh '''
          docker run --rm \
            --network ci \
            -v "$WORKSPACE":/work -w /work \
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
