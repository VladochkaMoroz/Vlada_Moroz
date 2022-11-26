from behave import *
from chrome.main_class import TestWebPage

global test


@given('initialized driver')
def init_driver(context):
    global test
    test = TestWebPage()


@when('successful login')
def log_page(context):
    test.log_page()


@when('go to work shifts page')
def add_page(context):
    test.add_page()


@when('add new record')
def add_record(context):
    test.add_record()


@when('set work hours')
def set_clock(context):
    test.set_clock()

@when('save record')
def save_record(context):
    test.save_record()

@then('new work shift appeared')
def check_new_record(context):
    test.check_record()


@then('remove added record')
def del_record(context):
    test.del_record()

@then('check if record is removed')
def check_record_afterdelete(context):
    test.check_record_after()

@then('close page')
def close_page(context):
    test.close_page()