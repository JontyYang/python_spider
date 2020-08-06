__author__ = "jonty yang"
import threading
import time
# 多线程

# def coding():
#     for x in range(3):
#         print('coding %d' % x)
#         print('%s' % threading.current_thread())
#         time.sleep(1)
#
# def drawing():
#     for x in range(3):
#         print('drawing %d' % x)
#         print('%s' % threading.current_thread())
#         time.sleep(1)
#
# def main():
#     t1 = threading.Thread(target=coding)
#     t2 = threading.Thread(target=drawing)
#     t1.start()
#     t2.start()
#     print(threading.enumerate())   # 枚举线程

# 实现线程的封装
class codingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('coding %d' % x)
            print('%s' % threading.current_thread())
            time.sleep(1)

class drawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('drawing %d' % x)
            print('%s' % threading.current_thread())
            time.sleep(1)

def main():
    t1 = codingThread()
    t2 = drawingThread()
    t1.start()
    t2.start()
    print(threading.enumerate())

if __name__ == '__main__':
    main()