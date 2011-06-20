#!/usr/bin/python

contest_server = "contest.tuenti.net"
contest_path = "/"

import sys, subprocess

from http_requests import request, post_multipart

if (len(sys.argv) < 3):
	print "Usage:"
	print "   " + sys.argv[0] + " <challenge_token> </path/to/your/program>"
	print
	sys.exit(1)

args = sys.argv

args.pop(0)
token = args.pop(0)

def callbackInput(url, params, method, response):
	if (response.status != 200):
		print "We got an error from server. Ensure you are using a valid token."
		print "Response: " + response.read()
		sys.exit(response.status)

input = request(contest_server, contest_path + "?m=Solver&func=getTestInput", {"token":token}, "POST", callbackInput)

print ' '.join(args)
process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = process.communicate(input=input)[0]

def callbackOutput(url, params, method, response):
	if (response.status == 400):
		print "ERROR! Houston we have a problem!"
		print "--- INPUT ---------------------------------"
		print input
		print "--- OUTPUT CHECK --------------------------"
		print response.read()
	elif (response.status == 200):
		print "OK! Your program gives the right answer!"
		print "--- OUTPUT CHECK --------------------------"
		print response.read()
	else:
		print "We got an error from server. Ensure you are using a valid token."
		sys.exit(1)

request(contest_server, contest_path + '?m=Solver&func=assertTestOutput', {"token": token, "output": output}, "POST", callbackOutput)
