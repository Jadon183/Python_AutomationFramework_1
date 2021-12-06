from selenium import webdriver
import pytest
# import time
# import unittest
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
# import HtmlTestRunner
import allure
import moment
# class LoginTests(unittest.TestCase):
@pytest.mark.usefixtures("test_setup")
class TestLogin():
    #copied to conftest
    # #for all the function in class this fixture will work
    # @pytest.fixture(scope="class")
    # def test_setup(self):
    #     global driver
    #     driver=webdriver.Chrome(executable_path="C:\\Users\\lakshit.jadon\\PycharmProjects\\AutomationFramework_1\\drivers\\chromedriver.exe")
    #     driver.implicitly_wait(5)
    #     driver.maximize_window()
    #     yield
    #     driver.close()
    #     driver.quit()
    #     print("testcompleted")

    def test_login(self):
        driver=self.driver
        driver.get(utils.URL)
        login=LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver=self.driver
            homepage=HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x=driver.title
            # assert x == "abc"
            assert x == "orangeHRM"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime= moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName=utils.whoami()
            screenshotName=testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name="screenshotName",attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:\\Users\\lakshit.jadon\\PycharmProjects\\AutomationFramework_1\\screenshots "+screenshotName+".png")
            raise
        except:
            print("Some exception occurred")
            currTime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshotName",
                          attachment_type=allure.attachment_type.PNG)

            raise
        else:
            print("No exception occured")
        finally:
            print("I am inside finally block")

# if __name__=='main':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/lakshit.jadon/PycharmProjects/selenium/reports'),verbosity=2)