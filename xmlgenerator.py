

from headers import *
from methods import *
from all_mime_types import mime_types
import subprocess
import random

import datetime

from languages import *
from hashlib import md5
import base64
import os
import json


# ['A-IM', 'Accept', 'Accept-Charset', 'Accept-Datetime', 'Accept-Encoding', 'Accept-Language', 'Access-Control-Request-Headers', 'Access-Control-Request-Method', 'Authorization', 'Cache-Control', 'Connection', 'Content-Encoding', 'Content-Length', 'Content-MD5', 'Content-Type', 'Cookie', 'Date', 'Expect', 'Forwarded', 'From', 'HTTP2-Settings', 'Host', 'If-Match', 'If-Modified-Since', 'If-None-Match', 'If-Range', 'If-Unmodified-Since', 'Max-Forwards', 'Origin', 'Pragma', 'Prefer', 'Proxy-Authorization', 'Range', 'Referer', 'TE', 'Trailer', 'Transfer-Encoding', 'Upgrade', 'User-Agent', 'Via', 'Warning']


def aim(body=None):
	# A-IM: vcdiff, gdiff
	# or feed

	things = ["vcdiff", "gdiff", "feed"]

	things = random.sample(things, random.randrange(1,len(things)))

	return ', '.join(things)

def accept(body=None):
	things = random.sample(mime_types, random.randrange(1,5))
	return ', '.join(things)



def random_dateformat():
	
	# Thu, 31 May 2007 20:35:00 GMT
	# date '+%d.%b.%Y %H:%M' --date="2012-06-13 09:16:16 EDT + 1 year"
	# date '+%a, %b.%Y %H:%M' --date="2012-06-13 09:16:16 EDT + 1 year"

	# date '+%a, %b %d %Y %H:%M' --date="2012-06-13 09:16:16 EDT + 1 year"

	# date '+%a, %b %d %Y %H:%M:%S GMT' --date="2012-06-13 09:16:16 EDT + 1 year"

	# date '+%a, %b %d %Y %H:%M:%S GMT' --date="2007-05-31 20:35:00 GMT"

	# date '+%a, %d %b %Y %H:%M:%S GMT' --date="2007-05-31 20:35:00 GMT - 3 hours + 1 seconds"

	# date '+%a, %d %b %Y %H:%M:%S GMT' --date="1970-01-01 00:00:00 GMT - 2 hours + 1 seconds"
	random_seconds = random.randrange(1, 1678361453)
	command = "date '+%a, %d %b %Y %H:%M:%S GMT' --date=\"1970-01-01 00:00:00 GMT - 2 hours + {} seconds\"".format(str(random_seconds))

	command_shit = command.split(" ")
	#print(' '.join(command_shit))
	#command_shit = ["date", "+%a, %d %b %Y %H:%M:%S GMT", "--date=\"1970-01-01 00:00:00 GMT - 2 hours + {} seconds\"".format(str(random_seconds))]  # this wont work :D

	command_shit = ["./script.sh", str(random_seconds)]

	date_string = subprocess.check_output(command_shit)
	#date_string = str(date_string)
	date_string = date_string.decode('ascii')
	date_string = date_string[:-1]
	#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	return date_string



def accept_charset(body=None):

	return "iso-8859-5"


def accept_datetime(body=None):

	random_time = random_dateformat()







	return random_time


def accept_encoding(body=None):




	'''
	Thanks to https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding
	Directives
gzip
A compression format that uses the Lempel-Ziv coding (LZ77) with a 32-bit CRC.

compress
A compression format that uses the Lempel-Ziv-Welch (LZW) algorithm.

deflate
A compression format that uses the zlib structure with the deflate compression algorithm.

br
A compression format that uses the Brotli algorithm.

identity
Indicates the identity function (that is, without modification or compression). This value is always considered as acceptable, even if omitted.
	'''

	encodings = ["gzip", "compress", "deflate", "br", "identity"]
	things = random.sample(encodings, random.randrange(1,5))
	return ', '.join(things)
	#return random.sample(encodings, random.randrange(1,len(encodings)))


def accept_language(body=None):

	return random.choice(languages)

def access_control_request_headers(body=None):
	return ', '.join(http_headers)


def access_control_request_method(body=None):
	return random.choice(methods)

def authorization(body=None):

	return "Basic YWxhZGRpbjpvcGVuc2VzYW1l"

def cache_control(body=None):
	return "no-cache"

def connection(body=None):
	return "close"

def content_encoding(body=None):
	encodings = ["gzip", "compress", "deflate", "br", "identity"]
	thing = random.choice(encodings)
	return thing


def content_length(body=None):
	if body:
		return str(len(body))
	else:
		return str(0)


def content_md5(body=None):
	if body:
		# (md5("aa".encode("utf-8"))).digest()

		result = base64.b64encode((md5(body.encode("utf-8"))).digest()).decode("ascii")
		return result
	else:
		result = base64.b64encode((md5(''.encode("utf-8"))).digest()).decode("ascii")
		return result

def generate_json():

	my_dict = {'foo': 42, 'bar': {'baz': "Hello", 'poo': 124.2}}
	my_json = json.dumps(my_dict)
	return my_json

def content_type(body=None):
	things = random.choice(mime_types)
	return things
	#return ', '.join(things)

import string

def rand_str(length):
	return ''.join([random.choice(string.ascii_letters) for _ in range(length)])
	#return ''.join([x for x in random.sample(string.ascii_letters, length)])


def gen_random_cookie():
	return rand_str(random.randrange(1,3))+str("=")+rand_str(random.randrange(1,3))+";"

def cookie(body=None):

	num_cookies = random.randrange(1,4)
	cookies_string = ''.join([gen_random_cookie() for _ in range(num_cookies)])
	if cookies_string[-1] == ";":
		cookies_string = cookies_string[:-1]
	return cookies_string

def date(body=None):
	random_seconds = random.randrange(1, 1678361453)
	command = "date '+%a, %d %b %Y %H:%M:%S GMT' --date=\"1970-01-01 00:00:00 GMT - 2 hours + {} seconds\"".format(str(random_seconds))

	command_shit = command.split(" ")
	#print(' '.join(command_shit))
	#command_shit = ["date", "+%a, %d %b %Y %H:%M:%S GMT", "--date=\"1970-01-01 00:00:00 GMT - 2 hours + {} seconds\"".format(str(random_seconds))]  # this wont work :D

	command_shit = ["./scriptnow.sh", str(random_seconds)]

	date_string = subprocess.check_output(command_shit)
	#date_string = str(date_string)
	date_string = date_string.decode('ascii')
	date_string = date_string[:-1]
	#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	return date_string

def expect(body=None):
	return "100-continue"
def forwarded(body=None):
	return ""

def from_header(body=None):
	return "a@b.com"
def proxy_authorization(body=None):
	return "Basic YWxhZGRpbjpvcGVuc2VzYW1l"

def range_header(body=None):
	if body == None:
		return "bytes=0:0"
	maximum = len(body)

	minimum = 1
	things = []
	number_ranges = random.randrange(1,3)
	for _ in range(number_ranges):
		start = random.randrange(minimum, maximum)
		if minimum == maximum:
			end = maximum
			
		else:
			end = random.randrange(start, maximum)
		minimum = end
		things.append("bytes="+str(start)+":"+str(end))

	return ", ".join(things)


def referer(body=None):
	# Referer: https://example.com/page?q=123

	return "http://127.0.0.1:8080/a?q=124214221214"

def te(body=None):
	'''
	Directives
compress
A format using the Lempel-Ziv-Welch (LZW) algorithm is accepted as a transfer coding name.

deflate
Using the zlib structure is accepted as a transfer coding name.

gzip
A format using the Lempel-Ziv coding (LZ77), with a 32-bit CRC is accepted as a transfer coding name.

trailers
Indicates that the client is willing to accept trailer fields in a chunked transfer coding.

q
When multiple transfer codings are acceptable, the q parameter of the quality value syntax can rank codings by preference.

	'''

	things = ["compress", "deflate", "gzip", "trailers", "chunked"]

	poopoo = random.sample(things, random.randrange(1,3))
	return ", ".join(poopoo)

def trailer(body=None):
	return "header-names"


def transfer_encoding(body=None):

	'''
	Transfer-Encoding: chunked
Transfer-Encoding: compress
Transfer-Encoding: deflate
Transfer-Encoding: gzip
	'''
	oof = ["chunked", "compress", "deflate", "gzip"]

	return ', '.join(random.sample(oof, random.randrange(1,len(oof))))

def upgrade(body=None):
	return "foo/2"

def user_agent(body=None):

	return "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

def via(body=None):
	return "localhost"

def warning(body=None):
	return "110 anderson/1.3.37 \"Response is stale\""

def host(body=None):
	return rand_str(1)



#  ['A-IM', 'Accept', 'Accept-Charset', 'Accept-Datetime', 'Accept-Encoding', 'Accept-Language', 'Access-Control-Request-Headers', 'Access-Control-Request-Method', 'Authorization', 'Cache-Control', 'Connection', 'Content-Encoding', 'Content-Length', 'Content-MD5', 'Content-Type', 'Cookie', 'Date', 'Expect', 'Forwarded', 'From', 'HTTP2-Settings', 'Host', 'If-Match', 'If-Modified-Since', 'If-None-Match', 'If-Range', 'If-Unmodified-Since', 'Max-Forwards', 'Origin', 'Pragma', 'Prefer', 'Proxy-Authorization', 'Range', 'Referer', 'TE', 'Trailer', 'Transfer-Encoding', 'Upgrade', 'User-Agent', 'Via', 'Warning']


header_handlers = [aim, accept, accept_charset, accept_datetime, accept_encoding, accept_language,access_control_request_headers,access_control_request_method, authorization, cache_control, connection, content_encoding, content_length, content_md5, content_type, cookie, date, expect, forwarded, from_header, proxy_authorization, range_header, referer, te, trailer, transfer_encoding, upgrade, user_agent, via, warning, host]

#print("len(http_headers) == "+str(len(http_headers)))
#print("len(header_handlers) == "+str(len(header_handlers)))
#print("http_headers inside generator: "+str(http_headers))
function_pointers = {http_headers[i]:header_handlers[i] for i in range(len(http_headers))}

# ['A-IM', 'Accept', 'Accept-Charset', 'Accept-Datetime', 'Accept-Encoding', 'Accept-Language', 'Access-Control-Request-Headers', 'Access-Control-Request-Method', 'Authorization', 'Cache-Control', 'Connection', 'Content-Encoding', 'Content-Length', 'Content-MD5', 'Content-Type', 'Cookie', 'Date', 'Expect', 'Forwarded', 'From', 'Pragma', 'Prefer', 'Proxy-Authorization', 'Range', 'Referer', 'TE', 'Trailer', 'Transfer-Encoding', 'Upgrade', 'User-Agent', 'Via', 'Warning']



#header_handlers = [aim, accept]


def fill_in_header(modify_chance, header, body=None,specific_val=None):

	if specific_val != None:
		return str(header)+str(": ")+str(specific_val)

	if random.random()<modify_chance:
		# modify header
		return str(header)+str(": ")+str(function_pointers[header](body))  # function pointer list :)

		
	else:
		# use default value:

		default_value = default_values[http_headers.index(header)]
		return str(header)+str(": ")+str(default_value)
	return


def generate_headers(num_headers, modify_chance, banned_headers=[], body=None, mandatory_headers=[]):
	output_list = []

	for mandatory_header in mandatory_headers:

		# this is to check if we want a specific value or if we can choose a value:
		if isinstance(mandatory_header, str):
			output_list.append(fill_in_header(modify_chance, mandatory_header,body=body))
		else:
			# assume that we want a specific value:
			value = mandatory_header[1]
			output = fill_in_header(modify_chance, mandatory_header[0], body=body ,specific_val=value)
			output_list.append(output)
			



	for _ in range(num_headers-len(mandatory_headers)):
		selected_header = random.choice(http_headers)
		while selected_header in banned_headers:
			selected_header = random.choice(http_headers)

		output_list.append(fill_in_header(modify_chance, selected_header,body=body))

	return "\x0d\x0a".join(output_list)


def generate_params():
	how_many = random.randrange(0,3)

	if how_many == 0:
		return ""
	result = "?"

	parameters = [str(rand_str(random.randrange(1,3)))+"="+str(rand_str(random.randrange(1,3))) for _ in range(how_many)]

	result+='&'.join(parameters)

	return result






def generate_start_line(files):

	method = random.choice(methods)

	resource = "/"+random.choice(files)
	#print(resource)

	parameters = generate_params()		
	http_string = "HTTP/1.1"
	end = "\x0d\x0a"



	return method+" "+str(resource)+str(parameters)+" "+str(http_string)+"\x0d\x0a"

def generate_body(json=False, xml=False):
	if xml:
		xmlTemplate = """<root>
    <person>
        <name>%(name)s</name>
        <address>%(address)s</address>
     </person>
</root>"""

		data = {'name':'anurag', 'address':'Pune, india'}
		return (xmlTemplate%data)
	elif json:
		return generate_json()
	return rand_str(random.randrange(0,200))


def generate_request(modify_chance, filething, banned_headers=[], mandatory_headers=[]):


	'''

	Transfer-Encoding: compress   is banned when the request is a GET request.


	'''

	get_banned_headers = ["Transfer-Encoding"]

	put_banned_headers = ["Transfer-Encoding"]

	start_string = generate_start_line(filething)
	
	selected_method = start_string.split(" ")[0]

	if selected_method == "GET":
		#banned_headers.append("Transfer-Encoding")

		banned_headers += get_banned_headers



	num_headers_thning = random.randrange(1,5)
	body = generate_body()
	request_headers = generate_headers(num_headers_thning,modify_chance,banned_headers=banned_headers, body=body, mandatory_headers=mandatory_headers)

	print("request_headers: "+str(request_headers))

	# regenerate body if xml or json. This of course messes up the MD5 header for example, but it is good enough for our purposes.
	

	if "xml" in request_headers:
		body = generate_body(xml=True)
	if "json" in request_headers:
		body = generate_body(json=True)


	return start_string+request_headers+"\x0d\x0a\x0d\x0a"+str(body)



if __name__=="__main__":
	
	files = os.listdir("/home/cyberhacker/httpd-lto/install/htdocs")
	#print(random_dateformat())
	#print("Headers: "+str(http_headers))

	banlist = ["Warning", "Via", "Forwarded"]

	mandatory_headers = ["Host", ["Content-Type", "application/xml"], ["Accept", "application/xml"]]




	#print(generate_headers(3,0.9,banned_headers=banlist))
	#print(generate_start_line(files))

	existing_corpus_files = os.listdir("/home/cyberhacker/Asioita/Hakkerointi/httpcorpus/corpus_output/HTTPcorpus/")

	cur_filename = str(len(existing_corpus_files)+3)



	how_many_requests = 100

	for _ in range(how_many_requests):



		output = generate_request(0.9, files, banned_headers=banlist, mandatory_headers=mandatory_headers)
		fh = open("./xmlrequests/"+str(cur_filename), "w+")

		fh.write(output)
		fh.close()

		cur_filename = str(int(cur_filename)+3)