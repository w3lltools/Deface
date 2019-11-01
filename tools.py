#!/usr/bin/env python
import socket
import sys
import httplib
from urlparse import urlparse
import time as t
import urllib2
from urllib2 import Request, urlopen, URLError
import os
os.system('cls') # clear windows
os.system('clear') # clear linux or mac os


negative = '\033[91m'
positive = '\033[32m'
wait = '\033[94m'
final = '\033[93m'
total_scanned_global=0
found_scanned_global=0

if sys.platform == "linux2" or sys.platform == "linux":
        R = ("\033[31m")
        W = ("\033[0;1m")
        B = ("\033[35m")
        G = ("\033[34m")
        glp = ("\033[2m")
        Y = ("\033[33;1m")
	wh=("\033[1;37m")
	gr=("\033[0;37m")
	p=("\033[0;35m")
	re=("\033[1;31m")
	Gre=("\033[1;32m")
	ye=("\033[1;33m")
	Pu=("\033[0;35m")
	Cy=("\033[0;36m")
	Ca=("\033[0;33m")
	Fiuscha=("\033[0;35m")
	bl=("\033[1;34m")
else:
        R = ""
        W = ""
        Y = ""
        B = ""
        G = ""
        glp = ""
	wh  = ""
	gr = ""
	p = ""
	re = ""
	Gre = ""
	ye = ""
	Pu = ""
	Cy = ""
	Ca = ""
	Fiuscha = ""
	bl = ""


def OpenLog(log_file_name):
        try:
                f = open(log_file_name, 'r')
                return f.read()
                f.close()
        except IOError:
                return "File" + log_file_name + "does not exist."

if __name__ == "__main__":
	print (Gre+"		 ____               ___                           "+B+"  ")
        print (Gre+"		/\  _`\           /'___\                          "+B+"  ")
	print (Gre+"		\ \ \/\ \     __ /\ \__/   __      ___     __     "+B+"  ")
        print (Gre+"		 \ \ \ \ \  /'__`\ \ ,__\/'__`\   /'___\ /'__`\   "+B+"  ")
        print (Y+"		  \ \ \_\ \/\  __/\ \ \_/\ \L\.\_/\ \__//\  __/   "+B+"  ")
        print (Y+"		   \ \____/\ \____\\ \_\\ \__/.\_\ \____\ \____\  "+B+"  ")
        print (Y+"		    \/___/  \/____/ \/_/ \/__/\/_/\/____/\/____/  "+B+"Tools")
	print (G+80*"=")
        print (R+"		[+] 		Create By NURMALA 		[+]"+B+" ")
        print (R+"		[+] Greetz To All Member W3LLSQUAD OFFICIAL	[+]"+R+" ")
	print (R+"		[+] 	   facebook.com/w3llsquadofficial       [+]"+R+" ")
	print (G+80*"=")
def menu():

    	print (B+"""
		1. Install SQL DORK
		2. Install Finger Shell Admin Log
		3. Install SQLmap
		4. Install Red_Hawk
		5. Hashbuster
--------------------------------------------------------------------------------
		99. Exit
================================================================================
""")

loop = True

while loop:
    menu()
    what = input("Choose: ")
    if what == "00":
        print("================================")
        print("This will install: nmap, hydra, sqlmap, metasploit, ngrok, angryFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit and viSQL with one click.")
        print("----------------")
        hm = input("[?] Do you want to continue? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Please put down you android and go to the toilet...")
            print("Because this will take a long time.")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] everything successfully installed :)")
            print("[+] Happy Hacking <3")
            print("========================================")
        else:
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/w3lltools/SQL-DORKING.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQL Dork installed successfully :)")
        print("[+] Go to SQL DORK folder and type 'python2 sqlmap.py' to start.")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/w3lltools/Finder.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Go to sqlmap folder and type 'python2 sqlmap.py' to start.")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Go to sqlmap folder and type 'python2 sqlmap.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK installed successfully :)")
        print("[+] Go to RED_HAWK folder and type 'php rhawk.php' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "99":
        print("Bye.")
        break
