import base64
from Crypto.Cipher import AES

def pad(s):
    bs = AES.block_size
    pad_num = bs - len(s) % bs
    return s + bytes([pad_num]) * pad_num

plain = ''
with open('./out.dsp', 'r') as f:
    plain = f.read()

raw = pad(plain.encode())
cipher = AES.new(b'TRoP4GWuc30k6WUp', AES.MODE_CBC, b'bP3crVEO6wABzOc0')
enc = base64.b64encode(cipher.encrypt(raw))

with open('./in.dsp', 'wb') as f:
    f.write(enc)