from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application



def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # Chrome Browser
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # Firefox Browser
    # context.driver = webdriver.Firefox()


    # Headless Mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver =  webdriver.Chrome(
    #     options=options
    # )

    # BrowserStack
    bs_user = 'user'
    bs_key = 'key'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    # BrowserStack Mobile
    options = Options()
    bstack_options = {
        "osVersion": "13.0",
        "deviceName": "Samsung Galaxy S20 Ultra",
        "realMobile": "true",
        "browserName": "Chrome",
        "projectName": "Reelly Tests",
        "buildName": "Mobile Android Run",
        "sessionName": scenario_name
    }

    # BrowserStack Web
    # options = Options()
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Tahoe",
    #     "browserVersion": "latest",
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name,
    # }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # Mobile emulation
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--window-size=375,812")
    #
    # context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
