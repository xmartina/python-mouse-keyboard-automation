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


def to_screen_edge():
    mouse.move(-1000, -1000, absolute=False, duration=.4)


duration_i = timeit.timeit(to_screen_edge, number=6)

# 190, 40,
# 190, 70


# def link_click_i():
#     mouse.move(180, 70, absolute=False, duration=.4)
#
#
# duration_l = timeit.timeit(link_click_i, number=6)


def to_screen_edge_x_rt():
    mouse.move(180, 1, absolute=False, duration=.4)


duration_x_rt = timeit.timeit(to_screen_edge_x_rt, number=6)


def to_screen_edge_y_bt():
    mouse.move(1, 70, absolute=False, duration=.4)


duration_y_bt = timeit.timeit(to_screen_edge_y_bt, number=6)