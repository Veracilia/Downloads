#First HTTP Server
import socket;
#Define the host as a tuple
HOST, PORT = "", 8080;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1);
s.bind((HOST,PORT));
s.listen(True);

print("Serving HTTP on port %s...." %PORT);

while True:
    client_connection, client_address = s.accept();
    request = client_connection.recv(1024); #Buffer Size
    print(request.decode("utf-8")); #Display the HTTP request
    #Define the Web response message
    http_reponse = "HTTP/1.1 200 OK \n\n<html>" \
    "<head>" \
    "<title>PI2004K</title>" \
    "<style>"\
    "table, th , td {border: 1px solid black;}"\
    "</style>"\
    "</head>" \
    "<body>" \
    "<section>"\
    "<p style=color:purple;font-size:50px;font-family:courier;><strong>Welcome To Our Project!</strong></p>" \
    "</section>" \
    "<table style=width:100%;border:1px solid black;border-collapse:collapse;>"\
    "<tr>"\
    "<th>Name</th>"\
    "<th>Age</th>"\
    "<th>Hobby</th>"\
    "</tr>"\
    "<tr>"\
    "<td>Han Wen</td>"\
    "<td>19</td>"\
    "<td>Watch anime, play games</td>"\
    "</tr>"\
    "<tr>"\
    "<td>Hannan</td>"\
    "<td>19</td>"\
    "<td>Gaming</td>"\
    "</tr>"\
    "<tr>"\
    "<td>Yi Sheng</td>"\
    "<td>22</td>"\
    "<td>Gaming</td>"\
    "</tr>"\
    "</table>" \
    "<p>&nbsp;</p>"\
    "<footer>" \
    "<a href=https://www.ite.edu.sg/ target=_blank>This is our school</a>"\
    "</footer>" \
    "<p>&nbsp;</p>" \
    "<aside>" \
    "<img src='https://i.imgur.com/xrVXDQ2.jpeg'>" \
    "</aside>" \
    "</body>" \
    "</html>" \




    client_connection.sendall(bytes(http_reponse, "utf-8"));
    client_connection.close();
