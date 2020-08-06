import threading

gLock = threading.Lock()
bLock = threading.Lock()
VALUE = 0
g = 9

# 锁机制
def add_value():
    global VALUE
    global g
    gLock.acquire()
    for x in range(10000000):
        VALUE += 1
        g += 1
    gLock.release()
    print(g)
    print(VALUE)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()
