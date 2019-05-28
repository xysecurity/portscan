import sys
import queue
import threading
import subprocess
class socket1():
	def __init__(self,target):
		self.target=target
		# print(target)
		

	def scan(self,ip):
		# print("start scan")

		# print(s.connect_ex((self.target,80)))
		# for i in range(1,100):
			# print(i)
		obj=subprocess.Popen(['ping',ip],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		stdout,stderr=obj.communicate()
		obj.wait()
		# print(stdout.decode('gbk'))
		if 'TTL' in stdout.decode('gbk'):
			print(ip,'存活')

	def worker(self,q):
		while not q.empty():
			ip=self.target+'.'+str(q.get())
			try:
				self.scan(ip)
			finally:
				q.task_done()
	# def main(self):
	# 	print("start to detect ",self.target)
	# 	loop=asyncio.get_event_loop()
	# 	tasks=[asyncio.ensure_future(self.scan(port)) for port in range(1,65536)]
	# 	loop.run_until_complete(asyncio.wait(tasks))
if __name__ == '__main__':
	print("Start testing the target ip scope")
	print("Example: 192.168.0")
	if len(sys.argv)!=2:
		print("format wrong")
		sys.exit()
	# iplist=[]
	q=queue.Queue()
	target=sys.argv[1]
	a=socket1(target)
	list(map(q.put,range(1,255)))
	threads=[threading.Thread(target=a.worker,args=(q,)) for i in range(200)]
	list(map(lambda x:x.start(),threads))

	q.join()
	print("scan over")

	# for i in range(10):
	# 	p=multiprocessing.Process(target=a.worker,args(i,q,))
	# 	p.start()

	

	
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
	

