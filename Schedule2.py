import schedule 
import time



def job():
    print("TEMPARETURE")

print("Measuring...")
schedule.every().day.at("21:18").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
