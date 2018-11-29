import os
import SimpleHTTPServer
import SocketServer

PORT = 8000

INDEX_HTML = """ <html>

<head>
    <title>Kubernetes Hack Session</title>
</head>

<body>
    <h1>Hello {}</h1>
    <img src=https://memegenerator.net/img/instances/80246929/you-get-kubernetes-everyone-gets-kubernetes.jpg>
</body>

</html>
"""
name = os.getenv("NAME", "")

INDEX_HTML = INDEX_HTML.format(name)

with open("index.html", "w") as f:
    f.write(INDEX_HTML)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
