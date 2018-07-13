from selenium import webdriver


def generate_token(echo=False):
    if echo:
        print("Generating new token....")
    url = "https://sigopt.com/getstarted"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get(url)

    tab = driver.find_elements_by_class_name('clickable-tab')[1]
    tab.click()
    submit = driver.find_element_by_class_name('modal-footer')
    while not submit.is_displayed():
        pass
    submit.click()
    while True:
        try:
            token = driver.find_element_by_class_name('hljs-string').text.strip('"')
        except Exception:
            continue
        if token:
            break
    driver.stop_client()
    if echo:
        print("New token generated: {}".format(token))
    return token

