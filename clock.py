from apscheduler.schedulers.blocking import BlockingScheduler as bs
import bin as bins
sched = bs()

@sched.scheduled_job('interval', minutes = 10)
def run():
    bins.bot.login_bot()
    bisn.bot.run_bot()
