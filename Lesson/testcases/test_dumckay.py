import pytest
from example1 import register_user as register
from example6 import register_user as error_empty
from example7 import register_user as gender_empty
from example8 import register_user as nick_empty
from example9 import register_user as email_empty
from example10 import register_user as mistake_password
from example11 import register_user as error_password2
from example12 import register_user as error_password

def test_user_registration():
    a = register()
    assert a[0] == a[1]

def test_user_registration_mistake_password():
    a = mistake_password()
    assert a[0] == a[1]

def test_user_registration_error_empty():
    a = error_empty()
    assert a[0] == a[1]

def test_user_registration_gender_empty():
    a = gender_empty()
    assert a[0] == a[1]

def test_user_registration_nick_empty():
    a = nick_empty()
    assert a[0] == a[1]

def test_user_registration_email_empty():
    a = email_empty()
    assert a[0] == a[1]

def test_user_registration_password2():
    a = error_password2()
    assert a[0] == a[1]

def test_user_registration_error_password():
    a = error_password()
    assert a[0] == a[1]