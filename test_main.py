import pytest
from main_class import TestWebPage

global test


def test_driver_init_():
    global test
    test = TestWebPage()


def test_lod_page():
    test.log_page()


def test_add_page():
    test.add_page()


def test_add_record():
    test.add_record()


def test_set_clock():
    test.set_clock()


def test_save_record():
    test.save_record()


def test_check_record():
    test.check_record()


def test_del_record():
    test.del_record()


def test_check_record_afterdelete():
    test.check_record_after()

def test_close_page():
    test.close_page()