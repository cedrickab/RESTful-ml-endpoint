/* Requires the Docker Pipeline plugin , blue ocean & ssh agent and git*/
pipeline {
    //agent any
    agent {docker { image '3.10.9-buster' }}
    environment {
        PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python37-32;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\mingw64\\bin;C:\\Program Files\\Git\\usr\\bin"
        }
    
    stages {
           stage('connexion'){      
           steps {
                git branch: 'main', credentialsId: 'SSH', url: 'git@github.com:cedrickab/RESTful-ml-endpoint.git'
                  }
                }
                  
        stage('Testing') {
            steps {
                bat 'python -m pip install Flask'
                bat 'python -m pip install numpy'
                bat 'python app.py'
                bat 'python Test.py'
            }
        }
        stage('building and running image') {
            steps {
                // build a Docker image
                bat 'docker build -t jenkis_tp .'
                // run a Docker container from the image
                bat 'docker run -d jenkis_tp'
            }
        }
        stage('dockerhub') {
            environment {
                dockerpass = credentials('dockerhubaccount')
                gitpass = credentials('gitaccount')
                }
            steps {
            //login
                   bat "docker login -u ${dockerpass_USR} -p ${dockerpass_PSW} "
                   // build a Docker image
                   bat 'docker image tag jenkis_tp cedrickab/endpoint:myfirstimage'
                   // run a Docker container from the image
                   bat 'docker image push cedrickab/endpoint:myfirstimage'
                    }
                }
    }
}
