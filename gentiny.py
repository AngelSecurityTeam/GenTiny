#!/usr/bin/env python3
#https://github.com/AngelSecurityTeam/GenTiny
import urllib.request, urllib.error, urllib.parse,urllib.request,urllib.parse,urllib.error,os,sys
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'
def GenTiny():
	 
    print("""{1}{2}{1}
╔═╗┌─┐┌┐┌╔╦╗┬┌┐┌┬ ┬
║ ╦├┤ │││ ║ ││││└┬┘
╚═╝└─┘┘└┘ ╩ ┴┘└┘ ┴  
  {0}{1}AngelSecurityTeam{2}
python3 gentiny.py URL 
""".format(end,bold,cyan))

url="http://tinyurl.com/api-create.php?url=" #API

if len(sys.argv) != 2:  #help
    GenTiny()
    sys.exit(0);
if str(sys.argv[1]).find("http://") == -1 and  str(sys.argv[1]).find("https://") == -1:
	sys.argv[1]="http://"+sys.argv[1]
req=urllib.request.urlopen(url+str(sys.argv[1]))
data=req.read()
print("""{1}{2}{1}
╔═╗┌─┐┌┐┌╔╦╗┬┌┐┌┬ ┬
║ ╦├┤ │││ ║ ││││└┬┘
╚═╝└─┘┘└┘ ╩ ┴┘└┘ ┴  
  {0}{1}AngelSecurityTeam{2}
python3 gentiny.py URL 
""".format(end,bold,cyan))
print("\033[0m\033[1m\033[36m~/Link# \033[0m\033[1m"+str(data))
