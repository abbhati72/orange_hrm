import datetime

from selenium import webdriver


class TakeScreenShoteUtil:

    @staticmethod
    def takeScreenShots(driver,filename):
    #def takeScreenShots(filename="demo"):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        scr_sts_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        print(scr_sts_datetime)
        path = "..\\ScreenShots\\testcase+" + str(filename) + "" + scr_sts_datetime + ".png"
        driver.save_screenshot(path)
        #return path


#TakeScreenShoteUtil.takeScreenShots()


# Get current time
#current_time = datetime.now()

# Format time using strftime
#formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")  # e.g., 2025-06-18_20-12-34
#print(formatted_time)

# Other common formats
#print(current_time.strftime("%H:%M:%S"))  # e.g., 20:12:34 (24-hour)
#print(current_time.strftime("%I:%M:%S %p"))  # e.g., 08:12:34 PM (12-hour with AM/PM)
#print(current_time.strftime("%Y%m%d_%H%M%S"))  # e.g., 20250618_201234 (compact)
