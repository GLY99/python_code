import queue
import traceback
from threading import Thread


class Worker(Thread):
    """
    Thread executing tasks from a given tasks queue
    """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self._stop = False
        self.start()

    def run(self):
        while not self._stop:
            try:
                func, args, kwargs = self.tasks.get(timeout=2)
                if func:
                    try:
                        func(*args, **kwargs)
                    except Exception as e:
                        print("work func error. %s" % traceback.format_exc())
                    self.tasks.task_done()
                else:
                    pass
            except queue.Empty:
                pass
            except Exception:
                print("Work thread error. %s " % traceback.format_exc())

    def stop(self):
        self._stop = True


class ThreadPool(object):
    """
    Pool of threads consuming tasks from a queue
    """

    def __init__(self, num_threads):
        self.task_queue = queue.Queue(num_threads)
        self.pool = []
        for _ in range(num_threads):
            self.pool.append(Worker(self.task_queue))

    def add_task(self, func, *args, **kargs):
        """
        Add a task to the queue
        """
        self.task_queue.put((func, args, kargs))

    def wait_completion(self):
        """
        Wait for completion of all the tasks in the queue
        """
        self.task_queue.join()

    def destroy_pool(self):
        for w in self.pool:
            w.stop()
        print("======= pool size: %d =======" % len(self.pool))

    def __del__(self):
        self.destroy_pool()


if __name__ == '__main__':
    from random import randrange
    from time import sleep
    delays = [randrange(1, 10) for i in range(100)]

    def wait_delay(d):
        print('sleeping for (%d)sec' % d)
        sleep(d)


    # 1) Init a Thread pool with the desired number of threads
    pool = ThreadPool(20)

    for i, d in enumerate(delays):
        # print the percentage of tasks placed in the queue
        print('%.2f%c' % ((float(i) / float(len(delays))) * 100.0, '%'))
        # 2) Add the task to the queue
        pool.add_task(wait_delay, d)

    # 3) Wait for completion
    pool.wait_completion()
    pool = None
    print("end")
