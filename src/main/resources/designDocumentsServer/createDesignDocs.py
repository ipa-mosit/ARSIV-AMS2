import os
import glob
import re
import subprocess
import http.server
import socketserver

# os.system("source ../../../../venv/bin/activate")
# os.system("ls")
os.chdir("markdowns")
files=glob.glob("*.md")
os.chdir("../web")
i=0
print(os.path.dirname("/home/osman/.vim/templates"))
dirname=os.path.join("/home/osman/.vim/templates","ertan")
print(dirname)
while i<len(files):
    fileName=files[i].split(".")[0]+".html"
    print(fileName)
    print(os.getcwd())
    os.system('pandoc -t html5 --css ../bulma.css ../markdowns/%s -s -o %s --metadata pagetitle="Documentation Server" --filter pandoc-plantuml' % (files[i],fileName))
    i+=1
# Server yapılandırması
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
