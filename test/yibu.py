import asyncio
import time

look = asyncio.get_event_loop()

async def asy():
    i.append(1)
    return  i

i = []
print(time.time())

for item in range(20000):
    look.run_until_complete(asy())
print(i)