#!/bin/bash

sudo apt update

sudo apt-get install -y python3.8

sudo rm /usr/bin/python3

sudo ln -s python3.8 /usr/bin/python3

sudo apt install -y python3-pip python3.8-dev

sudo apt install -y nginx

sudo apt install -y virtualenv