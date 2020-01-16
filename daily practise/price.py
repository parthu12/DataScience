from selenium import webdriver
amazonURL='https://www.amazon.in/Java-Concurrency-Practice-1-Goetz/dp/9332576521/ref=sr_1_1?crid=8RJQSKDRRUK0&keywords=concurrency+in+practice&qid=1579139949&sprefix=concurre%2Caps%2C292&sr=8-1'
amazonSelector = '#soldByThirdParty > span.a-size-medium.a-color-price.inlineBlock-display.offer-price.a-text-normal.price3P'
browser = webdriver.Firefox()
browser.get(amazonURL)
price = browser.find_element_by_css_selector(amazonSelector)
print(price.text)
