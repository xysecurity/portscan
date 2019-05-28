import socket
import asyncio
import sys
class socket1():
	def __init__(self,target):
		self.target=target
		# print(target)
		

	async def scan(self,ip):
		# print("target:",ip)
		s=socket.socket()
		s.settimeout(0.1)
		# print(s.connect_ex((self.target,80)))
		# for i in range(1,100):
			# print(i)

		if s.connect_ex((self.target,ip))==0:
			print(ip,'open')
		s.close()
	def main(self):
		print("start to detect ",self.target)
		loop=asyncio.get_event_loop()
		tasks=[asyncio.ensure_future(self.scan(port)) for port in range(1,65536)]
		loop.run_until_complete(asyncio.wait(tasks))
		print("scan over")
if __name__ == '__main__':
	print("Start testing the target port")
	# print("Example:['127.0.0.1','127.0.0.2'] 80")
	if len(sys.argv)!=2:
		print("format wrong")
		sys.exit()
	iplist=[]
	target=sys.argv[1]
	# for i in sys.argv:
	# 	iplist.append(i)
	# del iplist[0]
	# print(iplist)
	# port=int(sys.argv[1])
	# del iplist[-1]
	# print(port)
	a=socket1(target)
	a.main()
	# a.scan(80)
	# for i in range(1,100):
	# 	a.scan(i)
	

