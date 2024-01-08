#!/bin/bash
apt-get install -y sudo
sudo apt-get install -y nodejs
sudo apt-get install -y npm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 12.11.1
npm install -g n
n 6.11.3