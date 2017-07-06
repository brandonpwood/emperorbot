from apscheduler.schedulers.blocking import BlockingScheduler as bs

sched = bs()

@sched.scheduled_job('interval', minutes = 3)
def timed_job():
  r = bot.login_bot()
  bot.run_bot(r)
  print("Updating...")
sched.start()
