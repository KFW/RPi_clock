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

LOGIN_URL = 'http://1.1.1.1/fs/customwebauth/login.html?aswitch_url=http://1.1.1.1/login.html&client_mac=a8:66:7f:2f:02:37&wlan=Guest&redirect=google.com/'  # noqa
GOOGLE = 'http://google.com'

def internet_on():
    with Browser('chrome') as browser:
        browser.visit(GOOGLE)
        sleep(3)
        return (browser.title == 'Google')

def main():
    if not internet_on():
        print('not connected')
        with Browser('chrome') as browser:
            browser.visit(LOGIN_URL)
            sleep(3)
            if browser.is_text_present('Agreement', wait_time=7):
                print('clicking')
                browser.find_by_name('Submit').first.click()
                sleep(5)

#############################################################################

if __name__ == "__main__":
    main()
