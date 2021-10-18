from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get(r"http://8.129.91.152:8765/ ")
driver.implicitly_wait(1.5)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/span[1]/a").click()
driver.find_element_by_id("phone").send_keys("13139181550")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/input").send_keys(input())
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/a").click()
text=driver.find_element_by_xpath("//*[@class='layui-layer-content']").text
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/input").send_keys(text[-4:])
print(text[-4:])
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("qazxswedc123")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
driver.find_element_by_xpath("/html/body/div[4]/div[3]/a[1]").click()
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/span[3]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/a/img").click()
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[1]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/div[1]/div/input").send_keys("张已")
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/div[2]/div/input").send_keys("37252219700421611X")
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/div[3]/div/button").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div[2]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/a").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/div[2]/div/input[2]").send_keys("中国银行")
driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/div[3]/div/input").send_keys("372522197406087218")
driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/div[4]/div/div[1]/select").send_keys("北京")
driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/div[5]/div/input").send_keys("宇宙")
driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/div[6]/div/button").click()





