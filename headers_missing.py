header_string = '''A-IM
Accept
Accept-Charset
Accept-Datetime
Accept-Encoding
Accept-Language
Access-Control-Request-Method
Access-Control-Request-Headers
Authorization
Cache-Control
Connection


Content-Encoding
Content-Length
Content-MD5
Content-Type
Cookie
Date
Expect
Forwarded
From
Host


HTTP2-Settings
If-Match
If-Modified-Since
If-None-Match
If-Range
If-Unmodified-Since
Max-Forwards
Origin
Pragma
Prefer
Proxy-Authorization
Range
Referer
TE


Trailer
Transfer-Encoding


User-Agent
Upgrade


Via
Warning
'''


default_values_string = '''A-IM: feed
Accept: text/html
Accept-Charset: utf-8
Accept-Datetime: Thu, 31 May 2007 20:35:00 GMT
Accept-Encoding: gzip, deflate
Accept-Language: en-US
Access-Control-Request-Method: GET

Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Cache-Control: no-cache
Connection: keep-alive

Connection: Upgrade 
Content-Encoding: gzip
Content-Length: 348
Content-MD5: Q2hlY2sgSW50ZWdyaXR5IQ==
Content-Type: application/x-www-form-urlencoded
Cookie: $Version=1; Skin=new;
Date: Tue, 15 Nov 1994 08:12:31 GMT
Expect: 100-continue
Forwarded: for=192.0.2.60;proto=http;by=203.0.113.43 Forwarded: for=192.0.2.43, for=198.51.100.17
From: user@example.com
Host: en.wikipedia.org:8080

Host: en.wikipedia.org
HTTP2-Settings: token64
If-Match: "737060cd8c284d8af7ad3082f209582d"
If-Modified-Since: Sat, 29 Oct 1994 19:43:31 GMT
If-None-Match: "737060cd8c284d8af7ad3082f209582d"
If-Range: "737060cd8c284d8af7ad3082f209582d"
If-Unmodified-Since: Sat, 29 Oct 1994 19:43:31 GMT
Max-Forwards: 10
Origin: http://www.example-social-network.com
Pragma: no-cache
Prefer: return=representation
Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Range: bytes=500-999
Referer: http://en.wikipedia.org/wiki/Main_Page
TE: trailers, deflate


Trailer: Max-Forwards
Transfer-Encoding: chunked


User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0
Upgrade: h2c, HTTPS/1.3, IRC/6.9, RTA/x11, websocket


Via: 1.0 fred, 1.1 example.com (Apache/1.1)
Warning: 199 Miscellaneous warning
'''






headers = header_string.split("\n")


headers = [x for x in headers if x != ""]
#print("set(headers) == "+str(set(headers)))
headers = list(set(headers))
headers = sorted(headers)

#print(headers.index("Prefer"))
thingoof = headers[20:30+1]
headers = thingoof
print("headers: "+str(headers))
#print("thingoof : "+str(thingoof))
headers = list(set(headers) - set(thingoof))
headers = sorted(headers)

http_headers = headers
http_headers.append("Host")
#print("http_headers == " + str(http_headers))

default_values = default_values_string.split("\n")
default_values = [x for x in default_values if x != ""]
default_values = sorted(default_values)
#print("just sorted default_values: "+str(default_values))
default_values = [val[val.index(":")+2:] for val in default_values]
default_values = list(default_values)
default_values.append("127.0.0.1:8080")




#print(default_values)






# this file basically exports the headers and their default values


