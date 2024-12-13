import concurrent.futures
import random
import time
import multiprocessing

class Driver(object):
    def __init__(self):
        pass

    def create(self):
        return random.randint(1, 10)

class Test(object):
    def __init__(self):
        self.driver = Driver()

    def create(self):
        t = self.driver.create()
        time.sleep(t)
        print(t)

    def multi_create(self, num):
        fs = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=num) as executor:
            for i in range(num):
                fs.append(executor.submit(self.create))
        for f in concurrent.futures.as_completed(fs):
            f.result()

    def test(self):
        # 进程池1
        fs = []
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            for _ in range(2):
                fs.append(executor.submit(self.multi_create, 2))
        for f in concurrent.futures.as_completed(fs):
            f.result()
        # 进程池2
        # pool = multiprocessing.Pool(2)
        # pool.map(self.multi_create, [2, 2])
        # pool.close()
        # pool.join()

if __name__ == "__main__":
    t = Test()
    t.test()