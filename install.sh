#!/bin/bash
sudo apt install python3 -y
sudo mkdir /usr/share/ramusql
sudo mv main/ main.py run.sh /usr/share/ramusql
sudo chmod 777 /usr/share/ramusql/run.sh
sudo ln -s /usr/share/ramusql/run.sh /usr/bin/ramusql
sudo mv ./install.sh /usr/share/ramusql
echo -e "\nRequirements installation completed! \nSetup has successfully installed! \nTry using this application with 'ramusql' command"