import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen(2)
server_ip = "92.10.10.10"
server_mac = "00:00:0A:BB:28:FC"
router_mac = "05:10:0A:CB:24:EF"
while True:
    routerConnection, address = server.accept()
    if(routerConnection != None):
        print(routerConnection)
        break