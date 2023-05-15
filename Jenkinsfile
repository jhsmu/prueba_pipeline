pipeline {

    agent any

    environment{
        DB_HOST="host.docker.internal"
        DB_PORT="8889"
        DB_NAME="prueba"
        DB_USER="root" 
        DB_PASSWORD="root"
    }

    stages{
        stage('build imagen'){
            steps{
                script{
                    //docker.build("conexion:latest","-f /Users/Kometsales/Desktop/git/prueba_pipeline/Dockerfile .")
                    sh 'docker build -t db_conexion . '
                }
            }
        }
        stage('execute conexion container'){
            steps{
                script{
                sh "docker run --rm db_conexion -e DB_HOST=${DB_HOST} -e DB_PORT=${DB_PORT} -e DB_NAME=${DB_NAME} -e DB_USER=${DB_USER} -e DB_PASSWORD=${DB_PASSWORD} python conexion.py -d" 
                }
            }
        }

    }
}