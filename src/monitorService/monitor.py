import subprocess

def monitorStatus():
	status = {}

	popen = subprocess.Popen(("cat /proc/meminfo | grep MemAvailable | cut -d ':' -f 2"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	avail_mem = (popen.stdout.read()).strip()
	avail_mem = avail_mem.split(' ')[0]
	status['ava_ram'] = avail_mem

	popen = subprocess.Popen(("df -h | grep /dev/xvda1 | awk {'print $4'}"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	status['ava_storage'] = popen.stdout.read()[:-2]

	return status

if __name__=="__main__":
	print monitorStatus()	

