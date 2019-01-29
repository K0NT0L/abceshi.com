 #!/usr/bin/env python2

'''
# Ehem'-'
# Mau ngapain stah?'-'
# W joned Tamvans:*
# klo mampir itu ngopi dulu dund ^_^
# Heleh W nuub ea qimack!!!
'''

takeover = """\033[92m
_____     _           ___
|_   _|_ _| | _____   / _ \__   _____ _ __
  | |/ _` | |/ / _ \ | | | \ \ / / _ \ '__|
  | | (_| |   <  __/ | |_| |\ V /  __/ |
  |_|\__,_|_|\_\___|  \___/  \_/ \___|_|

Creator = StarFuckTak'-'
Coder = python2
github = https://github.com/K0NT0L
"""
red = '\033[31;1m'
green = '\033[32;1m'
yellow = '\033[33;1m'
blue = '\033[34;1m'
purple = '\033[35;1m'
cyan = '\033[36;1m'
white = '\033[37;1m'

import requests, threading, os, sys, time
os.system("clear")

print takeover

print 55*"\033[34;5m="
print(purple),("Contoh:  \033[33;5mgrab.github.io")
nuub = raw_input("\033[32;5mTarget Domain/IP: \033[31;5m")
req = requests.get("https://api.hackertarget.com/reverseiplookup/?q=" + (nuub))
tu = open("Voss.txt", "w")
tu.write(req.text)
tu.close
cok = open("Voss.txt", "r")
cad = open("Voss.txt", "r")
leno = cad.read().split()
print(blue),("Total Web: \033[37;5m" + str(len(leno)))
hoho = len(leno)
time.sleep(0.5)
bgsd = "Bangsad lu muehehehe"
print ("\033[32;5m[\033[33;5m+\033[32;5m]\033[37;5mWaiting For Get \033[31;5m404 \033[37;5mWeb....\033[00m")
print 55*"\033[32;5m_"
def mulai(tek):
        global p
        p = 0
        while True:
          try:
            p +=1
            yah = cok.readline().strip()
            v = "http://" + (yah)
            try:
              cat = requests.get(v)
            except:
              continue
            if p > hoho:
                print ("\033[32;5m[!]Selesai")
                sys.exit()
            if cat.status_code ==404:
                print ("\033[34;5m" + yah + " \033[35;5m>> \033[31;5m404")
                continue
            else:
               continue
          except KeyboardInterrupt:
            print("\033[31;5m[!]Keluar\033[00m")
            sys.exit()
threads = []
for x in bgsd:
    t = threading.Thread(target=mulai, args=(bgsd,))
    threads.append(t)
    t.start()
for t in threads:
    t.join
