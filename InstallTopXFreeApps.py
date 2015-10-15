import uiautomator,os,sys,datetime,time
from uiautomator import Device

device='null'

def intializtion():
	global device
	print 'Getting Device Info'
	os.system('adb devices > deviceinfo')
	devinf = open('deviceinfo','rb')
	dev = devinf.readlines()[1].split('\t')[0]
	print dev
	devinf.close()
	device=Device(dev)

def launch_store():
	global device
	print 'Launching Playstore'
	os.system('adb shell am start -n com.android.vending/com.google.android.finsky.activities.MainActivity')
	while True :
		if device(text="APPS").exists :
			device(text="APPS").click()
			print "Success ; APPS Tab Launched"
			time.sleep(1)
			break
	while True :
		if device(text="TOP FREE").exists :
			device(text="TOP FREE").click()
			print "Success ; TOP FREE Tab Launched"
			time.sleep(1)
			break
def install(n):
	global device
	lastnum=n-2
	num=str(n)
	num=num+"."
	while True :
		if device(textStartsWith=num).exists :
			device(textStartsWith=num).click()
			print "Success ; APP%s Details Launched" % n
			time.sleep(1)
			break
		else :
#			device(textStartsWith=lastnum).swipe.up(steps=400)
			device().scroll.vert.forward(steps=1000)
			
	install_needed=0		
	while True :
		if device(text="OPEN").exists :
			print "Already Installaed Skipping Installation of APP %s" % n
			time.sleep(2)	
			break
		if device(text="INSTALL").exists :
			device(text="INSTALL").click()
			install_needed=1
			print "Success ; APP%s Install Clicked; Waiting for permission accept.." % n
			time.sleep(2)	
			break
		if device(description='Cancel this download' , className='android.widget.ImageView').exists :
			print "Already installation in progress Skipping Installation of APP %s" % n
			time.sleep(2)	
			break
	
	if install_needed :
		while True :
			if device(text="ACCEPT").exists :
				device(text="ACCEPT").click()
				print "Success ; Installing APP%s " % n
				time.sleep(2)	
				break
			if device(text="PROCEED").exists :
				device(text="PROCEED").click()
			if device(text="OK").exists :
				device(text="OK").click()
				break

	'''
	os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
	os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
	os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
	os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
	os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
	os.system("adb shell input keyevent KEYCODE_ENTER") 
	print "Success ; Installing Game%s .." % n
	'''
		
	'''
	while True :
		if device(text="OPEN").exists :
			device(text="OPEN").click()
			time.sleep(10)
			print "Success ; Installation of  Game%s Complete.." % n
			break
	'''
	device.screenshot("APP"+str(n)+".jpg")
	print 'Going back to APP list'
	device.press.back()
#	os.system("adb shell am force-stop com.android.vending")

def main():
	intializtion()
	launch_store()
	if sys.argv==2 :
		print 'Installing Top %s Apps ' % sys.argv[2]
		n=int(sys.argv[1])
	else :
		print 'Default : Installing Top 50 Apps '
		n=50
	for i in xrange(1,n+1):
		print "Install APP %s  " % i
		install(i)
	
	print "Done, Installation"		

'''
current_time = datetime.datetime.now().time()
current_date = datetime.datetime.now().date()
timestamp = current_date.isoformat()+'-'+current_time.isoformat().split('.')[0].replace(':','-')
'''

if __name__=='__main__':
	main()
