import random
import hashlib

message = b"Hello, World!"
hash_value = hashlib.sha256(message).hexdigest()
print('Hash value for original message:', hash_value)
received_message = b"Hello, World!"
hash_value_check = hashlib.sha256(received_message).hexdigest()
print('Hash value for received message: ',hash_value_check)
if hash_value == hash_value_check:
  print('Message integrity verified')
else:
  print('Failed')