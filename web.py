from http.server import HTTPServer, BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html>
    <header>
        <h3>
            <div align="center">
                Protocols in TCP/IP Protocol Suite.
            </div>
        </h3>
    </header>
    <body bgcolor="aqua">
        <br>
        <br>
        <div align="center">

        
        <table border="10" cellpadding="10" cellspacing="10" bgcolor="lightgreen">
            <tr>
                <td>
                    S.NO
                </td>
                <td align="center">
                    TCP/IP LAYER
                </td>
                <td align="center">
                    PROTOCOLS
                </td>
                
            </tr>
            <tr>
                <td align="center">
                    1
                </td>
                <td align="center">
                    APPLICATION LAYER
                </td>
                <td align="center">
                    HTTP, SMTP, DNS, FTP, SSH
                </td>
                </tr>
                <tr>
                    <td align="center">
                        2
                    </td>
                    <td align="center">
                        TRANSPORT LAYER
                    </td>
                    <td align="center">
                        TCP, UDP, SCTP
                    </td>
                </tr>

                <tr>
                    <td align="center">
                        3
                    </td>
                    <td align="center">
                        INTERNET LAYER
                    </td>
                    <td align="center">
                        IP, ICMP, ARP, RARP
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        4
                    </td>
                    <td align="center">
                        NETWORK ACCESS LAYER
                    </td>
                    <td align="center">
                        PPP, IEE 802.2, ETHERNET
                    </td>
                </tr>
                
        </table>
    </div>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()