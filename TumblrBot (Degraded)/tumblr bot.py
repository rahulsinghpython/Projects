# from bs4 import BeautifulSoup
# from urllib.request import urlopen as uReq
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains as actions

searchresult = input("what search result would you like?")
loops = 0

myurl = "https://www.tumblr.com/search/fitness"
driver = webdriver.Chrome("J:\python\chromedriver.exe")
driver.get(myurl)

login = driver.find_element_by_css_selector(".signup_link.login-button")
login.click()

time.sleep(2)

email = driver.find_element_by_id("signup_determine_email")
# email = driver.find_element_by_css_selector(".form_row.form_row_email")
email.send_keys("", Keys.RETURN) # INSERT EMAIL IN BETWEEN THE ""

time.sleep(1)

password = driver.find_element_by_id("signup_password")
password.send_keys("", Keys.RETURN) # INSERT PASSWORD IN BETWEEN THE ""

# time.sleep(1)

search = driver.find_element_by_id("search_query")
search.send_keys(searchresult, Keys.RETURN)

time.sleep(1)



def reblogging():
    global loops
    reblog = driver.find_elements_by_css_selector(".post_control.post-control-icon.reblog")


    for button in reblog:

        if loops >= 20:
            break

        button.click()
        time.sleep(2)


        try:
            closecaption = driver.find_element_by_class_name("reblog-list")
            hov = actions(driver).move_to_element(closecaption)
            hov.perform()
            closebutton = driver.find_element_by_xpath(
                """//*[@id="search_actions_search"]/div[9]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/span""")
            closebutton.click()
        except:
            print("no button")

        caption = driver.find_element_by_css_selector(".editor.editor-richtext")
        caption.send_keys("Follow us at MightyFitness")
        for i in range(13):
            caption.send_keys(Keys.LEFT_SHIFT, Keys.ARROW_LEFT)
        caption.send_keys(Keys.CONTROL, "k")
        time.sleep(1)
        mightyurl = driver.find_element_by_xpath(
            """(//INPUT[@type='text'])[2]""")
        #old one
        # mightyurl = driver.find_element_by_xpath("""//*[@id="search_actions_search"]/div[9]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div[2]/input""")
        mightyurl.send_keys("https://mightyfitness.tumblr.com", Keys.RETURN)

        tags = driver.find_element_by_xpath("""//*[@id="search_actions_search"]/div[9]/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/div[1]""")
        hashtags = ["#fitness", "#muscle", "#summerbody", "#inspiration", "#hot", "gym", "workout"]
        for tag in hashtags:
            tags.send_keys(tag, Keys.RETURN)

        publish = driver.find_element_by_xpath("""//*[@id="search_actions_search"]/div[9]/div/div/div/div/div[2]/div[2]/div/div[5]/div[1]/div/div[3]/div/div/button""")
        publish.click()

        time.sleep(3)

        loops += 1
        print(loops)




        # selectMighty = driver.find_element_by_tag_name("p")
        # actions.click_and_hold(selectMighty)



        # ActionChains.send_keys('dummydata')
        # ActionChains.perform()
        # caption = driver.find_element_by_css_selector("editor-richtext")
        # caption.send_keys("follow me at MightyFitness")

        #//*[@id="search_actions_search"]/div[9]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div[2]/input
reblogging()
