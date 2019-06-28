"""
webconnect.py
checks for web connection on guest network
if not present, goes to login page and clicks through

based on:
https://pythonadventures.wordpress.com/2011/11/30/autoconnect-to-wifi-in-my-hotel/
https://splinter.readthedocs.io/en/latest/
"""

from splinter.browser import Browser
from time import sleep

#####################################################################
# *** NOTE: will need to fix MAC address in URL on each machine *** #
#####################################################################

AUTHENTICATE_URL = 'http://1.1.1.1/fs/customwebauth/login.html?aswitch_url=http://1.1.1.1/login.html&client_mac=b8:27:eb:0a:9a:80&wlan=Guest&redirect=https://www.google.com/'  # noqa
GOOGLE = 'http://google.com'
DRIVER_PATH = {'executable_path':'/usr/lib/chromium-browser/chromedriver'}

def internet_on():
    with Browser('chrome', **DRIVER_PATH) as browser:
        browser.visit(GOOGLE)
        sleep(3)
        return (browser.title == 'Google')

def main():
    if not internet_on():
        print('not connected')
        with Browser('chrome', **DRIVER_PATH) as browser:
            browser.visit(AUTHENTICATE_URL)
            sleep(3)
            if browser.is_text_present('Agreement', wait_time=7):
                print('clicking')
                browser.find_by_name('Submit').first.click()
                sleep(5)

#############################################################################

if __name__ == "__main__":
    main()

