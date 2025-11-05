# 08 - Jenkins CI/CD

## Pipeline (declarative) example
```groovy
pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run Tests') {
      steps {
        sh 'pytest -q --maxfail=1'
      }
    }
  }
  post {
    always {
      junit 'reports/*.xml'
    }
  }
}
```

## GitHub webhook trigger
- In Jenkins job: enable "GitHub hook trigger for GITScm polling".
- Add webhook in GitHub repo settings pointing to `http://JENKINS_URL/github-webhook/`

## Run Pytest via Jenkins
- Use virtualenv on agent, install requirements, run pytest, archive reports.

## Schedule builds
- Use `Build periodically` with cron syntax in job config.