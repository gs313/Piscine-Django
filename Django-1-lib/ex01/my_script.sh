#!/bin/bash

echo "Current pip version:"
pip --version


echo "Installing path library..."
pip install git+https://github.com/jaraco/path.git --target local_lib --upgrade --force-reinstall > install.log 2>&1


if [ $? -eq 0 ]; then
    echo "Installation successful. Running my_program.py..."
    python3 my_program.py
else
    echo "Installation failed. Check install.log for details."
fi
