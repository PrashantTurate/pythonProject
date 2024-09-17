from BrowserPackage.OpenBrowser import start_browser
from BrowserPackage.CloseBrowser import close_browser

def testcase():
    start_browser()
    print("I am executing code TC1")
    close_browser()

testcase()