from apscheduler.schedulers.blocking import BlockingScheduler as bs
import bot
sched = bs()

@sched.scheduled_job('interval', minutes = 3)
def run():
    bot()
