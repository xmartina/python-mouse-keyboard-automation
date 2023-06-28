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


def mouse_scroll_top():
    mouse.move(-1000, -1000, absolute=False, duration=.4)


duration_mouse_scroll_top = timeit.timeit(mouse_scroll_top, number=2)


def mouse_scroll_middle():
    mouse.move(156, 170, absolute=False, duration=.4)


duration_mouse_scroll_middle = timeit.timeit(mouse_scroll_middle, number=2)


def mouse_scroll_d():
    mouse.wheel(-1)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


duration_mouse_scroll_d = timeit.timeit(mouse_scroll_d, number=38)


def mouse_scroll_u():
    mouse.wheel(1)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


duration_mouse_scroll_u = timeit.timeit(mouse_scroll_u, number=40)


def mouse_scroll_middle_i_sec_t():
    mouse.move(-156, 120, absolute=False, duration=.4)


duration_mouse_scroll_middle_i_sec_t = timeit.timeit(mouse_scroll_middle_i_sec_t, number=4)


def mouse_scroll_middle_ii_sec_t():
    mouse.move(270, -149, absolute=False, duration=.4)


duration_mouse_scroll_middle_ii_sec_t = timeit.timeit(mouse_scroll_middle_ii_sec_t, number=4)


def mouse_scroll_u_i_sec_t():
    mouse.wheel(-1)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


duration_mouse_scroll_u_i_sec_t = timeit.timeit(mouse_scroll_u_i_sec_t, number=4)


def mouse_scroll_middle_iii_sec_t():
    mouse.move(10, 50, absolute=False, duration=.4)


duration_mouse_scroll_middle_iii_sec_t = timeit.timeit(mouse_scroll_middle_iii_sec_t, number=5)


def mouse_click_i():
    mouse.click()


duration_mouse_click_i = timeit.timeit(mouse_click_i, number=2)
