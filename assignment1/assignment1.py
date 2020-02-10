from __future__ import unicode_literals

import redis

# fill in the following.
HOST = "redis-16933.c15.us-east-1-4.ec2.cloud.redislabs.com"
PWD = "yBFMT0bNR2mpF3HjviE45Ig9xGIPxKtI"
PORT = "16933"

redis1 = redis.Redis(host=HOST, password=PWD, port=PORT)

while True:
    msg = input("Please enter your query (type 'quit' or 'exit' to end):").strip()
    if msg == 'quit' or msg == 'exit':
        break
    if msg == '':
        continue
    print("You have entered " + msg, end=' ')

    # Add your code here

    try:
        X=redis1.get(msg)
        count=int(X.decode())
        redis1.incr(msg)
        print('for',count,' times')
    except:
        redis1.incr(msg)
        print('for zero times')

