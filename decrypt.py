import base64
from Crypto.Cipher import AES

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

dsp = ''
with open('./in.dsp', 'r') as f:
    dsp = f.read()

enc = base64.b64decode(dsp)
cipher = AES.new(b'TRoP4GWuc30k6WUp', AES.MODE_CBC, b'bP3crVEO6wABzOc0')
plain = unpad(cipher.decrypt(enc).decode())

with open('./out.dsp', 'w') as f:
    f.write(plain)
