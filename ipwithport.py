import socket
import asyncio
import sys
class socket1():
	def __init__(self,target,port):
		self.port=port
		self.target=target
		# print(target)
		

	async def scan(self,ip):
		# print("target:",ip)
		s=socket.socket()
		s.settimeout(1)	
		if s.connect_ex((ip,self.port))==0:
			print(ip,self.port,'open')
			s.close
	def main(self):
		loop=asyncio.get_event_loop()
		tasks=[asyncio.ensure_future(self.scan(ip)) for ip in self.target]
		loop.run_until_complete(asyncio.wait(tasks))
if __name__ == '__main__':
	print("Start testing the target port")
	# print("Example:['127.0.0.1','127.0.0.2'] 80")
	# if len(sys.argv)!=3:
	# 	print("format wrong")
	# 	sys.exit()
	iplist=[]

	for i in sys.argv:
		iplist.append(i)
	del iplist[0]
	print(iplist)
	port=int(sys.argv[-1])
	del iplist[-1]
	# print(port)
	a=socket1(iplist,port)
	a.main()
	

