pipeline {
  agent any

  stages {
    stage('Test') {
      steps {
        sh '''
          set -euxo pipefail
          echo "WORKSPACE=$WORKSPACE"
          ls -la

          docker run --rm --network ci \
            --volumes-from jenkins \
            -w "$WORKSPACE" \
            python:3.11-slim bash -lc '
              set -eux
              python -V
              ls -la
              test -f requirements.txt
              pip install -U pip
              pip install -r requirements.txt
              pytest -v --html=report.html --self-contained-html
            '
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
