#!/usr/bin/env groovy

/*** Variables ***/

// Parameters

def branch = params.branch


// For git
def gitCreds = 'derek'
def gitNgxSwag = 'github.com/dejonghe/picamtrigger.git'

node() {
    stage('prep') {
        dir('picamtrigger'){
            echo "Pulling picamtrigger code from branch \"${branch}\""
            checkout scm
            // git url: gitPiCamTrigger, credentialsId: gitCreds, branch: "${branch}"
        }
    }
    stage('build_dist') {
        dir('picamtrigger'){
            echo "Building picamtrigger"
            sh "python setup.py sdist"
        }
    }
    stage('deploy') {
        dir('picamtrigger'){
            sshagent(credentials: ['PiDeploy']) {
              sh 'scp dist/picamtrigger-0.0.0.tar.gz  -o StrictHostKeyChecking=no pi@192.168.1.137:/home/pi/'
              sh 'ssh pi@192.168.1.137 -o StrictHostKeyChecking=no "sudo pip3.6 install picamtrigger-0.0.0.tar.gz --force-reinstall --upgrade"'
            }
        }
    }
}
