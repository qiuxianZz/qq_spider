# import execjs
#
# js = '''function sun(a,b){
# return a + b
# }'''
#
#
# result = execjs.eval("1+1")
# print(result)
#
# aa = '''
# function test(a, b) {
#     return a * b;
# }'''
#
# res = execjs.compile(aa)
# result = res.call('test',8,9)
# print(result)

#!/usr/bin/env python3
# async.py
#!/usr/bin/env python3
# screenshot.py
from threading import Thread
from time import sleep
import numpy as np
import pandas as pd

def async_call(func):
    def wrapper(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

@async_call
def A(x1, x2, i):
    data = pd.DataFrame(np.random.randn(x1, x2))
    sleep(2)
    data.to_csv('data_{}.csv'.format(i))
    print ('data_{} save done.'.format(i))

def B(i):
    print ('B func ', i)

if __name__ == "__main__":
    for i in range(10):
        A(1000, 1000, i)
        B(i)