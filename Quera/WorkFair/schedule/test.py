import schedule
import time


def some():
    print("sss")


sh = schedule.Scheduler()
sh.every(2).to(4).seconds.do(some)

while True:
    sh.run_pending()
    print(sh.jobs)
    time.sleep(1)
