/* Requires the Docker Pipeline plugin , blue ocean & ssh agent and git*/


pipeline {
    agent any
    
    environment {
        PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python37-32;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\mingw64\\bin;C:\\Program Files\\Git\\usr\\bin"
        }
    
    stages {
           stage('connexion'){      
           steps {
                git branch: 'staging', credentialsId: 'SSH', url: 'git@github.com:cedrickab/TP_jenkins.git'
                  }
                }
                  
        stage('Testing') {
            steps {
                bat 'python -m pip install Flask'
                bat 'python test_main.py'
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
        stage('dockerhub and git') {
            environment {
                dockerpass = credentials('dockerhubaccount')
                gitpass = credentials('gitaccount')
                }
            parallel {
                stage("Build&push ") {
                    stages {
                        stage("dockerhub") {
                            agent any
                            steps {
                                //login
                                bat "docker login -u ${dockerpass_USR} -p ${dockerpass_PSW} "
                                // build a Docker image
                                bat 'docker image tag jenkis_tp cedrickab/tpjenkins_pipeline:myfirstimage'
                                // run a Docker container from the image
                                bat 'docker image push cedrickab/tpjenkins_pipeline:myfirstimage'
                                }
                            }
                        }
                    }
                stage("git&push") {
                    stages {
                        stage("merge main branch") {
                            agent any
                            steps {
                                sshagent(credentials:['SSH']){
                                    bat 'git checkout staging'
                                    bat 'git add -A' 
                                    bat 'git commit --allow-empty -am "Merged staging branch into main"'
                                    bat 'git remote set-url origin git@github.com:cedrickab/TP_jenkins.git'
                                    bat 'git checkout main'
                                    bat 'git pull'
                                    bat 'git merge origin/staging'
                                    // bat 'git commit -m "hello my commit message'
                                    bat 'git push origin main'

                                }
                        
                                }
                           }
                       }
                    }
                }
            }
    }
}
