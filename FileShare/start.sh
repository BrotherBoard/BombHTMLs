# server configration for FileShare
# open mobile hotspot before executing this file
# for AOSP, replace swlan0 with wlan1

su -c ip address add 1.1.1.1 dev swlan0
python3 FileShare.py
