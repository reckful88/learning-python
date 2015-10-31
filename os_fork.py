#encoding: utf-8
import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork() 	#制造一个新进程（子进程）
if pid ==0:
	print 'child process (%s) and my parent is %s.' % (os.getpid(),os.getppid())
else:
	print 'I (%s) just created a child process (%s).' % (os.getpid(),pid)

