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
}
