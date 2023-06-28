import random
import datetime
import timeit

# import event
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

# # Click Ads footer jumbo 1

Event().wait(3)


def mouse_scroll_top_p_ii():
    mouse.move(-1000, -1000, absolute=False, duration=.4)


duration_mouse_scroll_top_p_ii = timeit.timeit(mouse_scroll_top_p_ii, number=2)


# Nav to Jobs Catego
def mouse_nav_job_cat():
    mouse.move(37, 44, absolute=False, duration=.3)


duration_mouse_nav_job_cat = timeit.timeit(mouse_nav_job_cat, number=6)


def mouse_scroll_bt_inner():
    mouse.wheel(-.9)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
# duration_mouse_scroll_bt_inner = timeit.timeit(mouse_scroll_bt_inner, number=61)


duration_mouse_scroll_bt_inner = timeit.timeit(mouse_scroll_bt_inner, number=84)


def mouse_scroll_bt_inner_ii():
    mouse.wheel(.9)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
# duration_mouse_scroll_bt_inner = timeit.timeit(mouse_scroll_bt_inner, number=61)


duration_mouse_scroll_bt_inner_ii = timeit.timeit(mouse_scroll_bt_inner_ii, number=44)


def mouse_to_ads():
    mouse.move(-7, 85, absolute=False, duration=.09)


duration_mouse_to_ads = timeit.timeit(mouse_to_ads, number=3)
