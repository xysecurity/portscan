import socket
import asyncio
import sys
import multiprocessing
class socket1():
	def __init__(self,target):
		self.target=target
		# print(target)
		

	def scan(self,i):
		# print("start scan")

		# print(s.connect_ex((self.target,80)))
		# for i in range(1,100):
			# print(i)
		s=socket.socket()
		s.settimeout(0.1)
		if s.connect_ex((self.target,i))==0:
			print(i,'open')
			s.close()
	def worker(self,q):
		while not q.empty():
			port=q.get()
			try:
				self.scan(port)
			finally:
				q.task_done()
	def main(self):
		print("start to detect ",self.target)
		loop=asyncio.get_event_loop()
		tasks=[asyncio.ensure_future(self.scan(port)) for port in range(1,65536)]
		loop.run_until_complete(asyncio.wait(tasks))
if __name__ == '__main__':
	print("Start testing the target port")
	# print("Example:['127.0.0.1','127.0.0.2'] 80")
	if len(sys.argv)!=2:
		print("format wrong")
		sys.exit()
	# iplist=[]
	target=sys.argv[1]
	q=multiprocessing.JoinableQueue()
	a=socket1(target)
	p=multiprocessing.Pool()
	list(map(q.put,range(1,65535)))
	# for i in range(65535):
	# 	print(q.get())
	jobs=[multiprocessing.Process(target=a.worker,args=(q,)) for i in range(100)]
	list(map(lambda x:x.start(),jobs))
	print("scan over")

	

	
	# for i in sys.argv:
	# 	iplist.append(i)
	# del iplist[0]
	# print(iplist)
	# port=int(sys.argv[1])
	# del iplist[-1]
	# print(port)
	
	# a.scan(80)
	# for i in range(1,100):
	# 	a.scan(i)
	

