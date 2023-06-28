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


def keyboard_write():
    keyboard.send("f6", do_press=True, do_release=True)
    keyboard.write(text, delay=0.6, restore_state_after=True, exact=None)
    keyboard.send("enter", do_press=True, do_release=True)


def end_task():
    quit(mouse_control.shutdown())


mouse_control = BlockingScheduler()
mouse_control.add_job(open_browser, 'interval', seconds=3, id='open_browser')
mouse_control.add_job(keyboard_write, 'interval', seconds=20, id='my_job_id')
mouse_control.add_job(end_task, 'interval', seconds=45, id='end_task')

mouse_control.start()