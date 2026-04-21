import schedule 
import time
cnt = 0
def job():
    print("Hello!")
    global cnt 
    cnt+=1

schedule.every(2).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
    if cnt==5:
        break


