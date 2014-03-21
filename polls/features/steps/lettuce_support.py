from lettuce import after, world
from selenium import webdriver

def browser():
    if not hasattr(world, 'browser'):
        world.browser = webdriver.Firefox()
    return world.browser

@after.all
def close_browser(test):
    if hasattr(world, 'browser'):
        world.browser.quit()

def visit_url(url):
    browser().get('http://localhost:8000%s' % url)