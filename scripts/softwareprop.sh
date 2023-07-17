#!/bin/bash


apt update

sudo apt-get install -y software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update

sudo apt-get  install -y curl