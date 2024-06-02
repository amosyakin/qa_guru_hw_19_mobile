import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.feature('Android')
@allure.title('Поиск на сайте Wikipedia')
def test_search():
    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.feature('Android')
@allure.title('Переход по найденному элементу')
def test_open_page():
    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Python')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Python'))

    with step('Open first result'):
        results.first.click()


@allure.feature('Android')
@allure.title('Проверка стартового экрана')
def test_getting_started():
    with (step('Verify getting started page open')):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('The Free Encyclopedia'))

    with (step('Go to "New ways to explore" page')):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        with step('Verify "New ways to explore" page open'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                            ).should(have.text('New ways to explore'))

    with (step('Go to "Reading lists with sync page')):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        with step('Verify "Reading lists with sync" page open'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                            ).should(have.text('Reading lists with sync'))

    with step('Go to "Data & Privacy" page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        with step('Verify "Data & Privacy" page open'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                            ).should(have.text('Data & Privacy'))
