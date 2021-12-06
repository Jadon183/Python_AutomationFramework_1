import pytest
# for all the function in class this fixture will work
@pytest.fixture(scope="class")
def test_setup(request):
    #global driver
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:\\Users\\lakshit.jadon\\PycharmProjects\\AutomationFramework_1\\drivers\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
    print("testcompleted")
