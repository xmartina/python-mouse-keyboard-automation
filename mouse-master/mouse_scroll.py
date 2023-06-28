import mouse
import keyboard
from apscheduler.schedulers.background import BlockingScheduler


def mouse_scroll():
    mouse.wheel(-0.4)


def mouse_stop():
    mouse_control.pause_job('my_job_id')


def mouse_contenune():
    mouse_control.resume_job('my_job_id')


def end_task():
    quit(mouse_control.shutdown())


mouse_control = BlockingScheduler()
mouse_control.add_job(mouse_scroll, 'interval', seconds=0.5, id='my_job_id')
mouse_control.add_job(mouse_stop, 'interval', seconds=7)
mouse_control.add_job(mouse_contenune, 'interval', seconds=10)
# mouse_control.modify_job(mouse_scroll, id='my_job_id', 'interval', seconds=0.5,)
mouse_control.add_job(end_task, 'interval', seconds=15, id='job-end-resume')

mouse_control.start()
