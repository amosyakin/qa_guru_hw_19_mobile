import os
from pathlib import Path

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from qu_guru_hw_19_mobile import utils


context = os.getenv('context', 'bstack')
load_dotenv(Path(f'.env.{context}'))

remote_url = os.getenv('remote_url')
deviceName = os.getenv('deviceName')
udid = os.getenv('udid')
appWaitActivity = os.getenv('appWaitActivity')
app = os.getenv('app')
bstack_userName = os.getenv('bstack_userName')
bstack_accessKey = os.getenv('bstack_accessKey')


def to_driver_options():
    options = UiAutomator2Options()

    if context == 'device' or context == 'emulator':
        options.set_capability('udid', udid)
        options.set_capability('appWaitActivity', appWaitActivity)
        options.set_capability('remote_url', remote_url)
        options.set_capability('app', utils.file.abs_path_from_project(app))

    if context == 'bstack':
        options.set_capability('platformVersion', '9.0')
        options.set_capability('app', app)
        options.set_capability('deviceName', deviceName)
        options.set_capability('remote_url', remote_url)
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': bstack_userName,
                'accessKey': bstack_accessKey,
            },
        )

    return options
