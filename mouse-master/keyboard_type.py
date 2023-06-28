import webbrowser
import mouse
import keyboard
from apscheduler.schedulers.background import BlockingScheduler

text = "www.matagram.com"
urL = 'https://www.google.com'
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"


def open_browser():
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(urL)
    # webbrowser.get("google-chrome").open("elearning.wsldp.com/python3/")


def highlight_browser_address_bar():
    keyboard.send("f6", do_press=True, do_release=True)


def keyboard_write():
    keyboard.write(text, delay=0.2, restore_state_after=True, exact=None)
    keyboard.send("enter", do_press=True, do_release=True)


def open_browser_pause():
    keyboard_control.pause_job('open_browser')


def stop_f6_click():
    keyboard_control.pause_job('highlight_browser_address_bar')


def stop_open_browser_pause_process():
    keyboard_control.remove_job('pause_browser_open')


def open_browser_resume():
    # keyboard_control.resume_job('open_browser')
    keyboard.press("ctrl+t")
    keyboard.release("ctrl+t")


def end_task():
    quit(keyboard_control.shutdown())


keyboard_control = BlockingScheduler()
keyboard_control.add_job(open_browser, 'interval', seconds=3, id='open_browser')
keyboard_control.add_job(open_browser_pause, 'interval', seconds=4, id='pause_browser_open')
# keyboard_control.add_job(stop_open_browser_pause_process, 'interval', seconds=5, id='stop_pause_browser_open_process')
keyboard_control.add_job(highlight_browser_address_bar, 'interval', seconds=12, id='highlight_browser_address_bar')
keyboard_control.add_job(stop_f6_click, 'interval', seconds=13, id='stop_f6_click')
keyboard_control.add_job(keyboard_write, 'interval', seconds=16, id='my_job_id')
keyboard_control.add_job(open_browser_resume, 'interval', seconds=20, id='open_browser_resume')
keyboard_control.add_job(end_task, 'interval', seconds=450, id='end_task')

keyboard_control.start()
