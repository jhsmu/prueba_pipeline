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
                 sh 'docker build -t db_conexion .'
                    sh 'docker run -e DB_HOST=${DB_HOST} -e DB_PORT=${DB_PORT} -e DB_NAME=${DB_NAME} -e DB_USER=${DB_USER} -e DB_PASSWORD=${DB_PASSWORD} db_conexion '
                }
            }
        }
        
    }
}