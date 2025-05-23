# EX01 Developing a Simple Webserver
## Date: 28/04/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
```

## OUTPUT:
![alt text](<Screenshot 2025-04-28 at 2.14.09 PM.png>)
![alt text](<Screenshot 2025-04-28 at 2.21.35 PM.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
