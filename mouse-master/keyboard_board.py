import random
import datetime
import timeit

import mouse
from datetime import datetime
import keyboard
import time
import threading
from apscheduler.schedulers.background import BlockingScheduler
import multiprocessing
import sched
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from threading import Event
from itertools import repeat


def keyin_f5():
    # keyboard_control.resume_job('open_browser')
    keyboard.press("f5")
    keyboard.release("f5")


duration_y_bt = timeit.timeit(keyin_f5, number=6)
