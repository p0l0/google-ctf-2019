
 - Start the 'init_sat' executable an take the satelite name which is shown on the picture in the PDF, 'osmium'
 > # ./init_sat
> Hello Operator. Ready to connect to a satellite?
> Enter the name of the satellite to connect to or 'exit' to quit
> osmium
> Establishing secure connection to osmium
>  satellite...
> Welcome. Enter (a) to display config data, (b) to erase all data or (c) to disconnect
> 
> a
> Username: brewtoot password: ********************	166.00 IS-19 2019/05/09 00:00:00	Swath 640km	Revisit capacity twice daily, anywhere Resolution panchromatic: 30cm multispectral: 1.2m	Daily acquisition capacity: 220,000km²	Remaining config data written to: https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E
> 
> c
> Disconnecting, goodbye.
 - Under https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E we find a base64 encoded string which unfortunately is not what we are searching for
 - If we start the executable again an connect to osmium, and open a second shell and run a 'netstat':
> # netstat -an
> Active Internet connections (servers and established)
> Proto Recv-Q Send-Q Local Address           Foreign Address         State
> tcp        0      0 127.0.0.11:36139        0.0.0.0:*               LISTEN
> tcp        0      0 172.19.0.2:33702        xx.xx.xx.xx:80         TIME_WAIT
> tcp        0      0 172.19.0.2:51832        34.76.101.29:1337       ESTABLISHED
> udp        0      0 127.0.0.11:37537        0.0.0.0:*

 - We see a connection to '34.76.101.29' on port '1337', lets try to connect:

> # nc 34.76.101.29 1337
> Welcome. Enter (a) to display config data, (b) to erase all data or (c) to disconnect
>
>a
>Username: brewtoot password: CTF{4efcc72090af28fd33a2118985541f92e793477f}	166.00 IS-19 2019/05/09 00:00:00	Swath 640km	Revisit capacity twice daily, anywhere Resolution panchromatic: 30cm multispectral: 1.2m	Daily acquisition capacity: 220,000km²	Remaining config data written to: https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E
>
>c
>Disconnecting, goodbye.

- And there is our flag!

>CTF{4efcc72090af28fd33a2118985541f92e793477f}
