from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
# driver.find_element_by_xpath('//input[@id="kw"]').send_keys("新梦想")
# element=driver.find_element(By.XPATH,'//a[@name="tj_briicon"]')
# ActionChains(driver).move_to_element( element ).perform()   #鼠标移到更多上面
# time.sleep(2)
# driver.find_element(By.XPATH,'//div[@class="s-top-more-title c-font-normal c-color-t"]').click()

# element=driver.find_element(By.XPATH,'//img[@usemap="#mp"]')
# ActionChains(driver).context_click(element).perform()      #右击

# element=driver.find_element(By.XPATH,'//a[@href="https://www.hao123.com?src=from_pc"]')
# ActionChains(driver).click_and_hold(element).pause(10).release(element).perform()    #长按

# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys(Keys.TAB)  #键盘tab键操作
# time.sleep(2)
# #网页上的键盘操作，可以从当前位置出发，不是从元素位置出发
# ActionChains(driver).send_keys(Keys.TAB).perform()

# element=driver.find_element(By.XPATH,'//input[@id="kw"]')
# ActionChains(driver).click(element)\
#                     .pause(1).send_keys(Keys.TAB)\
#                     .pause(1).send_keys(Keys.TAB)\
#                     .pause(1).send_keys(Keys.TAB)\
#                     .pause(1).send_keys(Keys.ENTER)\
#                     .perform()   #连续点三下tab再点回车

# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys(Keys.CONTROL,'V')  #复制
# 组合键实现复制 ctr+v
# driver.find_element(By.XPATH,'//input[@id="kw"]').click()
# ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
#
# driver.implicitly_wait(20)

#js属性
# driver.execute_script('alert("hello！！");')  #弹窗显示
# time.sleep(2)
# a=driver.find_element(By.XPATH,'//input[@value="百度一下"]')
# js='arguments[0].removeAttribute("value");'  #移除属性
# driver.execute_script(js,a)
# time.sleep(2)
# js1='arguments[0].setAttribute("value","亮宝宝搜索");'  #修改属性
# driver.execute_script(js,a)

#跳窗口
nowhandle=driver.current_window_handle  #获取当前页句柄
driver.find_element(By.XPATH,'//div[@aria-label="百度热搜"]').click()  #点击百度热搜，打开另一个页面
time.sleep(2)
allhandls=driver.window_handles   #获取所有页句柄
for hand in allhandls:
    if hand!=nowhandle:      #通过for循环便利所有句柄，不等于nowhandle的就是新的页面，因为只打开了两个页面
        driver.switch_to_window(hand)    #通过新句柄跳转到新的页面
        driver.find_element(By.XPATH,'//a[@href="/board?tab=game"]').click()   #点击游戏
        time.sleep(2)

for hand in allhandls:
    if hand==nowhandle:
        driver.switch_to_window(nowhandle)   #跳转到最开始的页面
        driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('selenium')
        time.sleep(2)
        driver.find_element(By.XPATH,'//input[@id="su"]').click()
time.sleep(2)
driver.quit()