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


# Page One Start one

def main_init_strt():
    def mouse_scroll_top():
        mouse.move(-1000, -1000, absolute=False, duration=.4)

    duration_mouse_scroll_top = timeit.timeit(mouse_scroll_top, number=2)

    def mouse_scroll_middle():
        mouse.move(156, 170, absolute=False, duration=.4)

    duration_mouse_scroll_middle = timeit.timeit(mouse_scroll_middle, number=2)

    def mouse_scroll_d():
        mouse.wheel(-1)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    duration_mouse_scroll_d = timeit.timeit(mouse_scroll_d, number=58)

    def mouse_scroll_u():
        mouse.wheel(1)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    duration_mouse_scroll_u = timeit.timeit(mouse_scroll_u, number=80)

    def mouse_scroll_middle_i_sec_t():
        mouse.move(-156, 120, absolute=False, duration=.4)

    duration_mouse_scroll_middle_i_sec_t = timeit.timeit(mouse_scroll_middle_i_sec_t, number=4)

    def mouse_scroll_middle_ii_sec_t():
        mouse.move(-10, 20, absolute=False, duration=.4)

    duration_mouse_scroll_middle_ii_sec_t = timeit.timeit(mouse_scroll_middle_ii_sec_t, number=4)

    # def mouse_click_i():
    #     mouse.click()
    #     keyboard.press("enter")
    #     keyboard.release("enter")
    #
    #
    # duration_mouse_click_i = timeit.timeit(mouse_click_i, number=2)

    # Page Two Start

    # Nav to Jobs Catego
    def mouse_nav_around():
        mouse.move(37, 44, absolute=False, duration=.3)

    duration_mouse_nav_around = timeit.timeit(mouse_nav_around, number=6)

    def mouse_scroll_top_p_ii():
        mouse.move(-1000, -1000, absolute=False, duration=.4)

    duration_mouse_scroll_top_p_ii = timeit.timeit(mouse_scroll_top_p_ii, number=2)

    # Nav to Logo
    # def mouse_nav_logo():
    #     mouse.move(40, 38, absolute=False, duration=.4)
    #
    #
    # duration_mouse_nav_logo = timeit.timeit(mouse_nav_logo, number=4)

    # Nav to Jobs Catego
    def mouse_nav_job_cat():
        mouse.move(37, 44, absolute=False, duration=.3)

    duration_mouse_nav_job_cat = timeit.timeit(mouse_nav_job_cat, number=6)

    def mouse_click_i():
        mouse.click()
        keyboard.press("enter")
        keyboard.release("enter")

    duration_mouse_click_i = timeit.timeit(mouse_click_i, number=2)

    Event().wait(8.5)

    def mouse_wheel_p_i_u():
        mouse.wheel(-1)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    duration_mouse_wheel_p_i_u = timeit.timeit(mouse_wheel_p_i_u, number=8)

    # Nav to Marketing Manager Job – Pepsi
    # def mouse_click_ii():
    #     mouse.click()
    #     mouse.click()
    #     keyboard.press("enter")
    #     keyboard.release("enter")
    #
    #
    # duration_mouse_click_ii = timeit.timeit(mouse_click_ii, number=1)

    def mouse_to_featured_img():
        mouse.click()
        mouse.click()
        # mouse.move(40, 60, absolute=False, duration=.09)
        keyboard.press("enter")
        keyboard.release("enter")

    duration_mouse_to_featured = timeit.timeit(mouse_to_featured_img, number=2)

    Event().wait(8)

    seq = [4, 5, 6, 8]
    rand_featr_img = random.choice(seq)

    def mouse_scroll_u_p_ii():
        mouse.wheel(-1)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    duration_mouse_scroll_u_p_ii = timeit.timeit(mouse_scroll_u_p_ii, number=rand_featr_img)

    def mouse_click_feat_img():
        mouse.click()
        mouse.click()

    duration_mouse_click_feat_img = timeit.timeit(mouse_click_feat_img, number=1)

    Event().wait(11)

    # # Click Ads footer jumbo 1

    def mouse_scroll_bt_inner():
        mouse.wheel(-.9)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    duration_mouse_scroll_bt_inner = timeit.timeit(mouse_scroll_bt_inner, number=63)

    def mouse_to_ads():
        mouse.move(-10, -9, absolute=False, duration=.09)

    duration_mouse_to_ads = timeit.timeit(mouse_to_ads, number=3)

    def click_ads_i():
        mouse.click()
        mouse.click()

    duration_click_ads_i = timeit.timeit(click_ads_i, number=4)

    # Click Ads footer jumbo 2

    def mouse_to_ads_i():
        mouse.move(-10, -9, absolute=False, duration=.09)

    duration_mouse_to_ads_i = timeit.timeit(mouse_to_ads_i, number=3)

    def click_ads_ii():
        mouse.click()
        mouse.click()

    duration_click_ads_ii = timeit.timeit(click_ads_ii, number=4)

    def mouse_to_ads_ii():
        mouse.move(4, 54, absolute=False, duration=.09)

    duration_mouse_to_ads_ii = timeit.timeit(mouse_to_ads_ii, number=3)

    def click_ads_iii():
        mouse.click()
        mouse.click()

    duration_click_ads_iii = timeit.timeit(click_ads_iii, number=4)

    def mouse_to_ads_ii_i():
        mouse.move(10, 16, absolute=False, duration=.09)

    duration_mouse_to_ads_ii_i = timeit.timeit(mouse_to_ads_ii_i, number=3)

    def click_ads_iv():
        mouse.click()
        mouse.click()

    duration_click_ads_iv = timeit.timeit(click_ads_iv, number=4)

    def mouse_to_ads_ii_ii():
        mouse.move(14, 12, absolute=False, duration=.09)

    duration_mouse_to_ads_ii_ii = timeit.timeit(mouse_to_ads_ii_ii, number=3)

    def click_ads_v():
        mouse.click()
        mouse.click()

    duration_click_ads_v = timeit.timeit(click_ads_v, number=4)

    def mouse_to_ads_ii_iii():
        mouse.move(31, -32, absolute=False, duration=.09)

    duration_mouse_to_ads_ii_iii = timeit.timeit(mouse_to_ads_ii_iii, number=3)

    def click_ads_vi():
        mouse.click()
        mouse.click()

    duration_click_ads_vi = timeit.timeit(click_ads_vi, number=4)

    def mouse_to_ads_ii_iv():
        mouse.move(67, 21, absolute=False, duration=.09)

    duration_mouse_to_ads_ii_iv = timeit.timeit(mouse_to_ads_ii_iv, number=3)

    def click_ads_vii():
        mouse.click()
        mouse.click()

    duration_click_ads_vii = timeit.timeit(click_ads_vii, number=4)

    # Nav on Ads Site

    def mouse_ads_i():
        mouse.wheel(-.9)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    duration_mouse_ads_i = timeit.timeit(mouse_ads_i, number=200)

    def mouse_ads_ii():
        mouse.move(-31, -32, absolute=False, duration=.09)

    duration_mouse_ads_ii = timeit.timeit(mouse_ads_ii, number=7)

    def mouse_ads_i_nx():
        mouse.wheel(-.9)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    duration_mouse_ads_i_nx = timeit.timeit(mouse_ads_i_nx, number=100)

    def mouse_ads_iii():
        mouse.move(2, 52, absolute=False, duration=.09)

    duration_mouse_ads_iii = timeit.timeit(mouse_ads_iii, number=7)

    def mouse_ads_iv():
        mouse.wheel(.9)
        mouse.click("left")
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    duration_mouse_ads_iv = timeit.timeit(mouse_ads_iv, number=10)

    def mouse_ads_v():
        mouse.move(34, -36, absolute=False, duration=.09)

    duration_mouse_ads_v = timeit.timeit(mouse_ads_v, number=7)

    def mouse_ads_vi():
        mouse.click("left")

    duration_mouse_ads_vi = timeit.timeit(mouse_ads_vi, number=1)

    def mouse_ads_vii():
        mouse.move(1000, -1000, absolute=False, duration=.09)

    duration_mouse_ads_vii = timeit.timeit(mouse_ads_vii, number=7)

    def mouse_ads_viii():
        mouse.move(-14, 15, absolute=False, duration=.09)

    duration_mouse_ads_viii = timeit.timeit(mouse_ads_viii, number=7)

    def mouse_ads_ix():
        mouse.click("left")

    duration_mouse_ads_ix = timeit.timeit(mouse_ads_ix, number=1)

    def mouse_ads_x():
        mouse.move(-10, 0.1, absolute=False, duration=.09)

    duration_mouse_ads_x = timeit.timeit(mouse_ads_x, number=5)

    def mouse_ads_xi():
        mouse.click("left")

    duration_mouse_ads_xi = timeit.timeit(mouse_ads_xi, number=1)

    def mouse_ads_xii():
        mouse.move(-6, 0.1, absolute=False, duration=.09)

    duration_mouse_ads_xii = timeit.timeit(mouse_ads_xii, number=5)

    def keyboard_site():
        keyboard.send("f6", do_press=True, do_release=True)

    duration_keyboard_site = timeit.timeit(keyboard_site, number=1)

    main_site_url = "https://docupdates.com/"

    def keyboard_site_i():
        Event().wait(2)
        keyboard.write(main_site_url, delay=0.2, restore_state_after=True, exact=None)
        keyboard.send("enter", do_press=True, do_release=True)

    duration_keyboard_site_i = timeit.timeit(keyboard_site_i, number=6)


itrat_job = BlockingScheduler()

itrat_job.add_job(main_init_strt, 'interval', seconds=4, id='my_job_id')

itrat_job.start()
