

def test_open_page(driver, url):
    driver.get(url)
    assert url in driver.current_url