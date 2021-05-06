import socket
import ssl
import base64

username = b"username@gmail"
password = b"password"
to = b"email@here"
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
hostname = 'smtp.gmail.com'
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((hostname, 587))
#Fillin end
recv = clientSocket.recv(4096).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
clientSocket.send(b'EHLO smtp.google.com\r\n')
recv1 = clientSocket.recv(4096).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
clientSocket.send(b'STARTTLS\r\n')
print(clientSocket.recv(4096).decode())
ws = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_TLSv1_2)
ws.send(b'AUTH LOGIN\r\n')
print(ws.recv(4096).decode())
ws.send(base64.b64encode(username)+b'\r\n')
print(ws.recv(4096).decode())
ws.send(base64.b64encode(password)+b'\r\n')
print(ws.recv(4096).decode())
# Send MAIL FROM command and print server response.
# Fill in start
ws.send(b'MAIL FROM: <' + username + b'>\r\n')
# Fill in end
recv2 = ws.recv(4096).decode()
print(recv2)
# Send RCPT TO command and print server response. 
# Fill in start
ws.send(b'RCPT TO: <' + to + b'>\r\n')
# Fill in end
recv3 = ws.recv(4096).decode()
print(recv3)
# Send DATA command and print server response. 
# Fill in start
ws.send('DATA\r\n'.encode())
# Fill in end
recv4 = ws.recv(4096).decode()
print(recv4)
# Send message data.
# Fill in start
ws.send(msg.encode())
# Fill in end
# Message ends with a single period.
# Fill in start
ws.send(endmsg.encode())
# Fill in end
recv5 = ws.recv(4096).decode()
print(recv5)
# Send QUIT command and get server response.
# Fill in start
ws.send('QUIT\r\n'.encode())
# Fill in end
recv6 = ws.recv(4096).decode()
print(recv6)