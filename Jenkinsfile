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
        stage('build container'){
            steps{
                script{
                    docker.build("conexion:latest","-f /Users/Kometsales/Desktop/git/prueba_pipeline/Dockerfile .")
                }
            }
        }
        stage('execute container'){
            steps{
                script{
                    docker.image("conexion:latest").run("-e DB_HOST=${DB_HOST} -e DB_PORT=${DB_PORT} -e DB_NAME=${DB_NAME} -e DB_USER=${DB_USER} -e DB_PASSWORD=${DB_PASSWORD} -d")
                }
            }   
        }

    }
}