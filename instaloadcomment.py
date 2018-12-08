from selenium import webdriver
import time
 
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/p/BrEa3l4HNbR/')
 
# click load more comments button
while(1==1):
    try:
        python_button = browser.find_elements_by_xpath('/html/body/span/section/main/div/div/article/div[2]/div[1]/ul/li[2]/button')[0]
        python_button.click()
    except IndexError:
        #print ("mew")
        break;

i = 2
while (i<=605):
    user = browser.find_elements_by_xpath('/html/body/span/section/main/div/div/article/div[2]/div[1]/ul/li[{0}]/div/div/div/h3/a'.format(i))[0]
    title = user.get_attribute("title")
    m = 1
    c = 0
    while(1==1):
        try:
            check = browser.find_elements_by_xpath('/html/body/span/section/main/div/div/article/div[2]/div[1]/ul/li[{}]/div/div/div/span/a[{}]'.format(i,m))[0]
            m = m+1
            amp = check.get_attribute("href")
            #print (amp)
            c = c+1
        except IndexError:
            #print ("mew")
            break;
    if (c>=3):
        print (title)
    i = i+1
