import random
import time
import threading
__author__ = 'Jonty yang'


# 基于lock下的生产者-消费者模式
gMoney = 1000
gCondition = threading.Condition()
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
            gCondition.acquire()
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            gCondition.notify_all()
            gCondition.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            while gMoney < money:     # 唤醒锁时，还需满足money>gMoney
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return       # 返回
                print('%s准备消费%d元钱,剩余%d元钱,不足！！！' % (threading.current_thread(), money, gMoney))
                gCondition.wait()     # 将当前线程阻塞，并释放锁,当被唤醒notify，会再次加锁
            gMoney -= money
            print('%s消费了%d元钱,剩余%d元钱' % (threading.current_thread(), money, gMoney))
            gCondition.release()
            time.sleep(0.5)


def main():
    for x in range(5):
        t = Producer(name='生产者线程%d' % x)
        t.start()
    for x in range(3):
        t = Consumer(name='消费者线程%d' % x)
        t.start()
    print(threading.enumerate())


if __name__ == '__main__':
    main()