import allure
import allure_commons
import pytest
from selene import browser, support
from appium import webdriver

import config
from qu_guru_hw_19_mobile.utils.attach import attach_screen, attach_video


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=config.to_driver_options()
        )
        browser.config.timeout = 10.0

        # browser.config._wait_decorator = support._logging.wait_with(
        #     context=allure_commons._allure.StepContext)

    yield

    attach_screen()

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id: ' + session_id):
        browser.quit()

    if config.context == 'bstack':
        attach_video(session_id)
