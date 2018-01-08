from subprocess import Popen
for x in range(1,20):
	run = ["firefox", "www.google.com"]
	Popen(run)

