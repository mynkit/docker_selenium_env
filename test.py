'''selenium環境が正しくできているか確認するためのスクリプト

Usage:
    # python3 test.py

Google
Google

と表示されれば成功
'''


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chromedriver_path = '/usr/local/bin/chromedriver'
o = Options()
o.add_argument('--headless')
o.add_argument('--disable-gpu')
o.add_argument('--no-sandbox')
o.add_argument('--window-size=1200x600')

"""
Sample test
"""
d = webdriver.Chrome(chromedriver_path, options=o)
d.get('https://www.google.com')
print(d.title)
d.quit()

"""
Use the Chrome DriverService.
https://chromedriver.chromium.org/getting-started
"""
s = Service(executable_path=chromedriver_path)
s.start()
d = webdriver.Remote(
    s.service_url,
    desired_capabilities=o.to_capabilities()
)
d.get('https://www.google.com')
print(d.title)
d.quit()
