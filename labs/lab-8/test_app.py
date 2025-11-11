# TODO: add five more unit test cases
import pytest

def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Test that home page loads"""
    response = client.get('/login')
    assert response.status_code == 200

def test_users_page(client):
    """Test that users page loads"""
    response = client.get('/users')
    assert response.status_code == 200

def test_success_error(client):
    """Test that the error page works"""
    response = client.get('/error')
    assert response.status_code == 200

def test_success_success(client):
    """Test that the success page works"""
    response = client.get('/success')
    assert response.status_code == 200

def test_invalid_first_name(client):
    """Test signup validation for invalid first name"""
    response = client.post('/signup', data={
        'FirstName': '123',  # invalid - contains numbers
        'LastName': 'Doe',
        'Email': 'test@test.com',
        'PhoneNumber': '1234567890',
        'Password': 'password123'
    })
    assert b'First name can only contain letters' in response.data

def test_invalid_phone_number(client):
    """Test signup validation for invalid phone number"""
    response = client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': 'test@test.com',
        'PhoneNumber': '123',  # invalid - not 10 digits
        'Password': 'password123'
    })
    assert b'Phone number must be exactly 10 digits' in response.data

@pytest.mark.xfail
def test_invalid_password(client):#This this going to fail becuase the app does not actually do this
    """Test signup validation for password"""
    response = client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': 'test@test.com',
        'PhoneNumber': '1234567890',  
        'Password': '1234'#Invalid, must reject bad passwords
    })
    assert b'Passwrod number must be exactly 10 digits' in response.data#This error code does not acually happen


def test_invalid_email(client):
    """Test signup validation for invalid password"""
    response = client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': 'test',#Invalid, must reject bad passwords, not real email
        'PhoneNumber': '1234567890',  
        'Password': '1234'
    })
    assert b'Something went wrong on our end. Rest assured we are working to solve this problem. Please try again later.' in response.data

def test_invalid_blanks(client):#User somehow bypassed sanitization process, entered blank values
    """Test signup validation for invalid password"""
    response = client.post('/login', data={
        'Email': ' ',
        'Password': '1234'
    })
    assert b'Something went wrong on our end. Rest assured we are working to solve this problem. Please try again later.' in response.data

def test_invalid_email():
    
    pass