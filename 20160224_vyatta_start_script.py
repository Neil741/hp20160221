20160224_vyatta_start_script.py

reference 陳沙克日志 鏡像和密碼
add script on Customization Script Source
#------------------
#!/bin/sh
passwd vyatta<<EOF
vyatta
vyatta
EOF
#------------------

add firefox account to synchronize website bookmark

'git'
add bookmark and login git website
apt-get install git
git config --global user.name "<使用者名字>"
git config --global user.email "<電子信箱>"
