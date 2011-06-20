#!/usr/bin/python

contest_server = "contest.tuenti.net"
contest_path = "/"

import sys, subprocess

from http_requests import request, post_multipart

if (len(sys.argv) < 4):
	print "Usage:"
	print "   " + sys.argv[0] + " <challenge_token> </path/to/source/package> </path/to/your/program>"
	print
	sys.exit(1)

args = sys.argv

args.pop(0)
token = args.pop(0)
program_src = args.pop(0)

def callbackInput(url, params, method, response):
	if (response.status != 200):
		print "We got an error from server. Ensure you are using a valid token."
		print "Response: " + response.read()
		sys.exit(response.status)

f = open(program_src, 'r')
file = { "file": program_src, "value": f.read() }
f.close()

upload = post_multipart(contest_server, contest_path + "?m=Solver&func=submitCode", {"token":token}, file, callbackInput)
print upload.read()

input = request(contest_server, contest_path + "?m=Solver&func=getSubmitInput", {"token":token}, "POST", callbackInput)

process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = process.communicate(input=input)[0]

def callbackOutput(url, params, method, response):
	if (response.status == 200):
		print "Challenge completed!!!"
		print "Go to the contest page and refresh status to continue!"
	else:
		print "ERROR: Unable to send your program output!"
		print "We got an error from server when sending the output. Try to re-submit it asap, time is counting!"
		sys.exit(1)

request(contest_server, contest_path + '?m=Solver&func=submitOutput', {"token": token, "output": output}, "POST", callbackOutput)

