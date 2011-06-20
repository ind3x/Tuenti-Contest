
import httplib, mimetypes, urllib 

def request(server, path, params, method = "POST", callback = None):
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	params = urllib.urlencode(params)
	connection = httplib.HTTPSConnection(server)
	connection.request(method, path, params, headers)
	response = connection.getresponse()
	if (callback != None):
		callback(path, params, method, response)
	data = response.read()
	connection.close()
	return data

def post_multipart(server, path, params, files, callback = None):
	content_type, body = encode_multipart_formdata(params, files)

	headers = {"content-type":content_type, "content-length": str(len(body))}
	connection = httplib.HTTPSConnection(server)
	connection.request("POST", path, body, headers)
	response = connection.getresponse()

	if (callback != None):
		callback(path, params, "POST", response)

	return response

def encode_multipart_formdata(fields, file):
	BOUNDARY = '---do-not-read-this-no-no-no--_$'
	CRLF = '\r\n'
	contents = []
	for key in fields.keys():
		value = fields[key]
		contents.append('--' + BOUNDARY)
		contents.append('Content-Disposition: form-data; name="%s"' % key)
		contents.append('')
		contents.append(value)

	filename = file['file']
	value = file['value']
	key = "source"

	contents.append('--' + BOUNDARY)
	contents.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
	contents.append('Content-Type: %s' % get_content_type(filename))
	contents.append('')
	contents.append(value)

	contents.append('--' + BOUNDARY + '--')
	contents.append('')
	body = CRLF.join(contents)
	content_type = 'multipart/form-data; boundary=%s' % BOUNDARY

	return content_type, body

def get_content_type(filename):
	return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

