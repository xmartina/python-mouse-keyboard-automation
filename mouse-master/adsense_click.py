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

starttime = time.time()


def mouse_scroll():
    mouse.wheel(-0.4)


def mouse_scroll_e():
    mouse.wheel(1)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


def function_to_repeat():
    mouse.wheel(-1)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


def mouse_to_top_right():
    mouse.move(13, -10, absolute=False, duration=.05)


duration = timeit.timeit(function_to_repeat, number=6)
duration_mouse_rt = timeit.timeit(mouse_to_top_right, number=2)
# Event().wait(10)
duration_i = timeit.timeit(mouse_scroll_e, number=6)

