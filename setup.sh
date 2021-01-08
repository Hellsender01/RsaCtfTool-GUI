#!/bin/bash

apt-get update
apt install git
apt install python3
apt install python3-pip
git clone https://github.com/Ganapati/RsaCtfTool.git /opt/rsactftool
sudo apt install libmpc-dev
pip3 install gmpy2==2.1.0a2
pip3 install -r /opt/rsactftool/requirements.txt
mv /opt/rsactftool/RsaCtfTool.py /opt/rsactftool/rsactftool
chmod +x rsactftool_gui.py
./rsactftool_gui.py
