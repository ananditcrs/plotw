pipeline {

  agent any
  parameters {
        string(name: 'IMAGE_NAME', defaultValue: 'plotwifeFlaskapp', description: 'Ume docker image name')
    }
environment {
    imagename = "${params.IMAGE_NAME}"
    registryCredential = '<your channel>'
    dockerImage = ''
  }  
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/ismailyenigul/hacicenkins.git', branch: 'master', credentialsId: 'your-github-user-token'])

      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
             dockerImage.push('latest')

          }
        }
      }
    }
    /*
    Just in case if you've deployed your container then you could test w/ it
    */
    stage('Test Deployed Containers') {
            steps {
                echo '..........................Testing Docker Container..........................'
                script {
                    def response_plotwise = sh 'curl http://plotwise-test.com:8090/plotwise'
                    def response_plotwise_world = sh 'curl http://plotwise-test.com:8090/world'

                    echo '=========================API Responce plotwise ===================' + response_plotwise
                    if (response_plotwise == "Success" ) {
                        echo "API Test request was successful"
                    }
                    else {
                        echo "API Test request error status : $status"
                    }
                    
                    echo '=========================API Responce world ===================' + response_plotwise_world
                    if(response_plotwise == "Success"){
                        echo "API Test request was successful"
                    } else {
                        echo "API Test request error status : $status"
                    }
                }
            }
    }

    stage('Finally Remove Unused docker image') {
      steps{
         sh "docker rmi $imagename:$BUILD_NUMBER"
         sh "docker rmi $imagename:latest"

      }
    }
  }
}