#!/bin/bash

REPO_URL="https://github.com/XXRadeonXFX/ci-cd-html-project.git"
DEPLOY_DIR="/var/www/html"

echo "Deploying the latest code..."

# Clone or pull instead of deleting everything
if [ -d "$DEPLOY_DIR/.git" ]; then
    cd $DEPLOY_DIR
    git pull
else
    rm -rf $DEPLOY_DIR
    git clone $REPO_URL $DEPLOY_DIR
fi

# Restart Nginx
sudo systemctl restart nginx

echo "Deployment completed successfully!"
