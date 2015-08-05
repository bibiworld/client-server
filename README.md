# client-server
simple client and server in python


Update in Aug 5th by evan69.
These two files are ready to be used to send strings.

Usage:

1.Xiao Pi Hai enters a commend "python standardserver.py (number)" in commend line.
(number) refers to the number of the port your server will bind to on your computer. You'd better use a number LARGER than 10000. Otherwise the port might have been used by your computer and it would cause your server out of work. And remember do NOT use numbers that are LARGER than 32767.

2.If you want to stop the server, enter ctrl+c.

3.Xiao Pi Hai needs to inform Barry Bai of the IP and the port he has set. Than Barry Bai enters a commend "python standardclinet.py (ip) (port)" in commend line, using the ip and port number Xiao Pi Hai has told him.

4.And you can connect each other. At this time Barry Bai can enter a string and the string will be sent to Xiao Pi Hai. Xiao Pi Hai should do sth to be string and return a string back to Barry Bai.

5.Connect stoped. standardclinet.py stops working and standardserver.py still works.
