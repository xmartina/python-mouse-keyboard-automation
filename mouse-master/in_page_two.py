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


# def mouse_click_i_p_ii():
#     mouse.click()
#
#
# duration_mouse_click_i_p_ii = timeit.timeit(mouse_click_i_p_ii, number=1)


def mouse_move_mid_p_ii():
    mouse.move(-86, 96, absolute=False, duration=.4)


duration_mouse_move_mid_p_ii = timeit.timeit(mouse_move_mid_p_ii, number=4)


def mouse_scroll_d_p_ii():
    mouse.wheel(-.8)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


duration_mouse_scroll_d_p_ii = timeit.timeit(mouse_scroll_d_p_ii, number=40)
