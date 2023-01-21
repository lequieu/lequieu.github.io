#!/bin/bash
rsync -avz --delete --exclude '*upload.sh*' --exclude 'sandbox-*' --exclude 'bootstrap-3.*' . lequieu_joshlequieu@ssh.phx.nearlyfreespeech.net:

