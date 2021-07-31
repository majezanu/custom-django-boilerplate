import random; 
import string; 
key="".join([random.SystemRandom().choice(string.digits + string.ascii_letters) for i in range(100)])
print(f"'{key}'")