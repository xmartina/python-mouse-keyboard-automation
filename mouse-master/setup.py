"""
Usage instructions:

- If you are installing: `python setup.py install`
- If you are developing: `python setup.py sdist --format=zip bdist_wheel --universal bdist_wininst && twine check dist/*`
"""
import mouse
import keyboard

# from setuptools import setup
# setup(
#     name='mouse',
#     version=mouse.version,
#     author='BoppreH',
#     author_email='boppreh@gmail.com',
#     packages=['mouse'],
#     package_data={'mouse': ['*.md']},
#     url='https://github.com/boppreh/mouse',
#     license='MIT',
#     description='Hook and simulate mouse events on Windows and Linux',
#     keywords = 'mouse hook simulate hotkey',
#
#     # Wheel creation breaks with Windows newlines.
#     # https://github.com/pypa/setuptools/issues/1126
#     long_description=mouse.__doc__.replace('\r\n', '\n'),
#     long_description_content_type='text/markdown',
#
#     install_requires=["pyobjc-framework-Quartz; sys_platform=='darwin'"], # OSX-specific dependency
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: Microsoft :: Windows',
#         'Operating System :: Unix :: MacOS',
#         'Programming Language :: Python :: 2',
#         'Programming Language :: Python :: 3',
#         'Topic :: Software Development :: Libraries :: Python Modules',
#         'Topic :: Utilities',
#     ],
# )
from apscheduler.schedulers.background import BlockingScheduler


def mouse_to_top_right():
    mouse.move(10000, -10000, absolute=False, duration=4.3)


def mouse_pos_one():
    mouse.move(-170, 270, absolute=False, duration=4.4)


def mouse_left_click():
    keyboard.press("ctrl")
    mouse.click("left")
    keyboard.release("ctrl")


def auto_change_proxy():
    keyboard.press("ctrl+shift+0")
    keyboard.release("ctrl+shift+0")


def func_on():
    # mouse_to_top_right()
    # mouse_pos_one()
    mouse_left_click()


# def new_mouse_move():
#     mouse.move(-10000, -100, absolute=False, duration=0.5)
#     mouse.click("left")


def pause_job():
    sched.pause()


def resume_job():
    quit(sched.shutdown())


sched = BlockingScheduler()
sched.add_job(func_on, 'interval', seconds=5, id='my_job_id')  # will do the print_t work for every 60 seconds
# sched.add_job(auto_change_proxy, 'interval', seconds=7.6, id='auto_change_ip')
# sched.add_job(pause_job, 'interval', seconds=5, id='job-end-trig')
# sched.add_job(print_t, 'interval', seconds=3, id='my_job_id_resume')
# sched.add_job(resume_job, 'interval', seconds=350, id='job-end-resume')

# sched.remove_job('my_job_id')
sched.start()
