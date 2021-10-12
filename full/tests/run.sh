#!/bin/bash
echo "Install python dependencies"
pip3 install -r ./requirements.txt


# run robot test base on input variables
echo "Running our test"
python3 -m robot \
    --console verbose \
    simpleS1.robot