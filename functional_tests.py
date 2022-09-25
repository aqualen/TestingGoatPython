# Let's Go!  https://www.obeythetestinggoat.com/book/chapter_01.html
# brew install firefox
# NOTE: Firefox via Homebrew though: brew puts the Firefox binary in a strange location, and it confuses Selenium.
#       You can work around it, but it’s simpler to just install Firefox in the normal way.
# brew install geckodriver
# python3 --version
# Python 3.9.13
# I reverted to using pyenv and python 3.7
# pip install "django<1.12" "selenium<4"
# django-admin.py startproject superlists .
# python manage.py runserver
# python functional_tests.py                  ## in another window...


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title