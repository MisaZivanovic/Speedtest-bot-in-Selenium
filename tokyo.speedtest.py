from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#adresa sajta
#website url
url='https://www.speedtest.net/'
x = webdriver.Chrome()
#comanda da bot otvori sajt
#starts chrome and goes to the url
x.get(url)
#opens a search input for the server
x.find_element_by_class_name('btn-server-select').click()
x.implicitly_wait(30)
#clicks on the input place for the search
x.find_element_by_id('host-search').click()
x.implicitly_wait(30)
#types in name of the server, notice that i didn't finish the word, this is because sometimes, 
#if i type in the whole word speedtest.com tends to bug out, and offer you something tottally strange
#like, Tokyo = Bangladesh, Ankara, Banja Luka ... however, if you type in a couple of letters it always
#yields a propper result
x.find_element_by_id('host-search').send_keys('Toky')
x.implicitly_wait(30)
#bira Tokyo, okozio sam se oko ovoga! videti drugi cell
#chooses Tokyo, i can not even tell you how many hours i spent over that next click, 
#but it was a great learning and researching experience. I intentionally left some older
#tries
#x.find_element_by_xpath("//div[@class='server-hosts-list']//ul[@data-view-name='serverCollection']//li[@data-model-cid='c113']//a[@data-server-id='15047']").click()
x.find_element_by_xpath("//span[@class='host-location'][contains(text(),'Tokyo')]").click()
#pritiska dugme i idemooooo
#presses the button, and it starts to measure the internet speed
x.find_element_by_class_name('js-start-test').click()
x.implicitly_wait(300)
#now these next ones i did for fun, so it clicks a button for sharing the result
x.find_element_by_xpath("//a[@title='Direct link to this result']//*[@class='svg-icon svg-icon-md']").click()
#after it opens the options it clicks the result I need for my job
x.find_element_by_xpath("//input[@id='share-web']").click()
#this control simulates ctrl+c, how great is this? :)
#i will add additional parts of code, because this is not the end.
x.find_element_by_xpath("//input[@id='share-web']").send_keys(Keys.CONTROL, 'c')
#what it does next is it closes speedtest, goes to the webpage of my work, locates the current, ongoing event
#and locates the place where to paste "send_keys(Keys.CONTROL, 'v')" the result, and fills in
#additional forms on that page and submits the result. 
