from apscheduler.schedulers.blocking import BlockingScheduler as bs
import logging

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)



sched = bs()

@sched.scheduled_job('interval', minutes = 3)
def timed_job():
  r = bot.login_bot()
  bot.run_bot(r)
  print("Updating...")
sched.start()
