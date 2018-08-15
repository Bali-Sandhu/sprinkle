from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from nose.tools import assert_equal, assert_true

@given(u'the Login form is displayed')
def step_login_form_displayed(context):
    context.browser.get('https://sprinkle-burn.glitch.me/')
    context.find_element(By.id, "login-form")
    assert_equal(context.browser.title, "Worlds Best App")

@when(u'I enter valid credentials')
def step_enter_valid_credentials(context):
    context.browser.get(context)
    context.find_element_by_name('email').send_keys('test@drugdev.com')
    context.find_element_by_name('password').send_keys('supers3cret')

    # email = context.find_element_by_name('email').send_keys('test@drugdev.com')
    # email.send_keys('test@drugdev.com')
    # password = context.find_element_by_name('password').send_keys('supers3cret')
    # password.send_keys('supers3cret')

@when(u'I submit the Login Form')
def step_i_submit_login_form(context):
    context.browser.get(context)
    context.browser.find_by_label('Login').click()
    # login = context.browser.find_by_label('Login')
    # login.click()

@then(u'a welcome message is displayed')
def step_welcome_message_displayed(context):
    context.browser.get(context)
    message = context.browser.find(By.xpath, '      Welcome Dr I Test')
    print message


@when(u'I submit the Login form without credential')
def step_submit_blank_form(context):
    context.browser.get('https://sprinkle-burn.glitch.me/')
    email.send_keys('')
    password.send_keys('')
    login.click()
    blank_error_message = context.browser.find_by_id('login-error-box')
    print blank_error_message
    email.clear()

@then(u'the user is presented with an error message')
def blank_error(context):
    context.browser.get('https://sprinkle-burn.glitch.me/')

# @when(u'the user enters password')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When the user enters password')



# @when(u'clicks Login')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When clicks Login')
#
#
# @then(u'the user is presented with a welcome message')
# def step_impl(context):
#     raise NotImplementedError(
#         u'STEP: Then the user is presented with a welcome message')
#
#
# @given(u'the user has the incorrect credentials')
# def step_impl(context):
#     raise NotImplementedError(
#         u'STEP: Given the user has the incorrect credentials')
#
#
# @then(u'the user is presented with a error message')
# def step_impl(context):
#     raise NotImplementedError(
#         u'STEP: Then the user is presented with a error message')
