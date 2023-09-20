import pytest
from selene import be, have, browser

def test_google_search_passed():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_google_search_failed():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ogerohoeueuwjdjoqhr').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Поиск неуспешный')



