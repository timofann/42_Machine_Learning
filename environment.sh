#!/bin/sh

if [ "${BASH_SOURCE-}" = "$0" ]; then
    echo "You must source this script: source $0" >&2
    exit 33
fi

PROJECT_PATH="/opt/goinfre/dedelmir/42_Machine_Learning"
HOME=$(echo ~)
INSTALL_PATH="/opt/goinfre/dedelmir"
MINICONDA_PATH="miniconda3/bin"
SCRIPT="Miniconda3-py37_23.1.0-1-MacOSX-x86_64.sh"
REQUIREMENTS="jupyter numpy pandas"
DL_LINK="https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-MacOSX-x86_64.sh"

if which python | grep --silent $INSTALL_PATH\0; then
    echo "good python version :)"
else
    if [ ! -f $INSTALL_PATH/$SCRIPT ]; then
        curl -LO $DL_LINK; fi
    if [ ! -d $INSTALL_PATH/$MINICONDA_PATH ]; then
        sh $SCRIPT -b -p $INSTALL_PATH"/miniconda3"; fi
    if ! echo $PATH | grep --silent $INSTALL_PATH/$MINICONDA_PATH; then
        export PATH=$INSTALL_PATH/$MINICONDA_PATH:$PATH; fi
        export MINICONDA=$INSTALL_PATH/miniconda3
#    conda install -y $(echo $REQUIREMENTS)
fi

if [ ! -d $PROJECT_PATH/condavenv ]; then
    conda create -y python=3.7 pip --prefix $PROJECT_PATH/condavenv; fi
if ! echo $PATH | grep --silent ^$PROJECT_PATH/condavenv/bin; then
    conda init --all
    conda activate $PROJECT_PATH/condavenv; fi