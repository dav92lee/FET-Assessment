#!/bin/bash

#Common Variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

createVEnv() {
    echo "Create Virtual Environment"
    sudo pip install virtualenv
    virtualenv venv
    if [ ! -d "$DIR/venv"]; then
        echo "Failed To Create Virtual Environemnt"
        exit
    fi
}

#promptBoost() {
    #while true; do
        #read -p "Do you have boost installed?"
        #case $yn in
            #[Yy]* ) break;;
            #[Nn]* ) exit;;
            #* ) echo "Please answer yes or no.";;
        #esac
    #done
#}

#installBoost() {
    #if [[ "$OSTYPE" == "linux-gnu"  ]]; then
        #echo "This is not supported -- please install Boost on your Linux and rerun script"
        #promptBoost
    #elif [[ "$OSTYPE" == "darwin"* ]]; then\
        #brew install boost --with-python
        #brew install boost-python
    #elif [[ "$OSTYPE" == "cygwin" ]]; then
        #echo "This is not supported -- please install Boost on your Windows and rerun script"
        #promptBoost
    #else
        #echo "OS not detected.  Please install Boost on your system and rerun script"
        #promptBoost
    #fi
#}

#installTorch() {
    #echo "Install Torch"
    #git clone https://github.com/torch/distro.git torch --recursive
    #cd torch; bash install-deps;
    #./install.sh
    #source ~/.bashrc
    #source ~/.zshrc
    #source ~/.profile
    #for NAME in dpnn nn optim optnet csvigo cutorch cunn fblualib torchx tds;
        #do luarocks install $NAME;
    #done
    #cd ..
#}

#installOpenFace() {
    #echo "==Install OpenFace=="
    #installTorch
    #git clone --recursive https://github.com/cmusatyalab/openface.git
    #cd openFace
    #sudo python2 setup.py install
    #cd ..
#}

initIndra() {
    echo "==Init Indra=="
    pip install -r $DIR/requirements.txt
    #installOpenFace
}

#Activate venv
cd $DIR
createVEnv
source "$DIR/venv/bin/activate"
initIndra
