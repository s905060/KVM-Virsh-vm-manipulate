#!/usr/bin/python
import sys, argparse, shlex, subprocess
__author__ = 'Jash Lee'

#Get argument
parser = argparse.ArgumentParser(description='This is a script to manipulate VM')
parser.add_argument('-c','--Command', help='Command for VM',required=True)
parser.add_argument('-p','--Path', help='Path to the VM',required=True)
parser.add_argument('-n','--Name', help='Name of the VM',required=True)
args = parser.parse_args()

#Run command line tool
if str(args.Command) in ("create", "destroy", "shutdown", "suspend", "resume", "autostart"):
	try:
		print 'virsh', str(args.Command), str(args.Path) + str(args.Name)
		subprocess.check_call(['virsh', str(args.Command), str(args.Path) + str(args.Name)])
	except Exception as e:
		print e
else:
	print "Invalid Command:", str(args.Command), "[create, destroy, shutdown, suspend, resume, autostart]"