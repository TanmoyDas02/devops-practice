#!/bin/bash

sudo apt-get update -y
sudo apt-get install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx

echo "<h1>Welcome to Terraform EC2 Instance</h1>" | sudo tee /var/www/html/index.html