from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# a = webdriver.Chrome()
#
# a.get("https://www.autohome.com.cn/car/#pvareaid=3311275")

# print(a.current_url)
# print(a.page_source)
# a.find_element_by_name("wd").send_keys("中国")
# a.find_element_by_id("su").click()

# for i in range(1,27):
    # print(i)
    # a.find_element_by_class_name("footer_auto").click()
    # time.sleep(1)



# b = a.find_element_by_class_name("footer_auto")
#
# ActionChains(a).move_to_element(b).perform()




#######################################
#凤勾情：弃后独步天下

driver = webdriver.Chrome()

driver.get("https://ac.qq.com/ComicView/index/id/629846/cid/1")

# a = driver.find_element_by_id("mainControlNext")
# ActionChains(driver).move_to_element(a).perform()

a = driver.find_element_by_tag_name("body")
a.click()

# driver.find_element_by_id("chapter").click()


for i in range(30):
    time.sleep(0.3)
    a.send_keys(Keys.SPACE)

print(driver.page_source)


next_1 = driver.find_element_by_id("mainControlNext")
ActionChains(driver).move_to_element(next_1).click(next_1).perform()

time.sleep(5)

driver.quit()






