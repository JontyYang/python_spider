import random
import time
import threading
__author__ = 'Jonty yang'


# 基于lock下的生产者-消费者模式
gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney        # 必读定义在run中
        global gTimes
        while True:
            money = random.randint(100, 1000)
            if gTimes >= gTotalTimes:
                break
            gTimes += 1
            gLock.acquire()
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if money <= gMoney:
                gMoney -= money
                print('%s消费了%d元钱,剩余了%d元钱' % (threading.current_thread(), money, gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print('%s准备消费%d元钱,剩余%d元钱,不足！！！' % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(0.5)


def main():
    for x in range(5):
        t = Producer(name='生产者线程%d' % x)
        t.start()
    print(threading.enumerate())
    for x in range(3):
        t = Consumer(name='消费者线程%d' % x)
        t.start()



if __name__ == '__main__':
    main()