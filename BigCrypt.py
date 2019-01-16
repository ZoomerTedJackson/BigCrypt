import hashlib
import sys

def bigHash(plaintext):
	times = 1000000000
	
	try:
		times = times * int(sys.argv[2])
	except:
		pass

	count = 0
	while count < times:
		plaintext = hashlib.sha224(plaintext)
		plaintext = plaintext.hexdigest()
		count = count + 1
	return plaintext

try: 
	f = open(str(sys.argv[1]),"w+")
except:
	print "To use Big-crypt: \n\n	Big-Crypt.py [plaintext txt file] [Num times to run]"

f.write(bigHash(f.read()))
f.close()