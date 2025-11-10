# TODO: add five more unit test cases

def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Test that login page loads"""
    response = client.get('/login')
    assert response.status_code == 200

def test_users_page(client):
    """Test that users page loads"""
    response = client.get('/users')
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
    
    # My 5 pytest below:
def test_valid_signup(client):
    """Test signup with valid data"""
    response = client.post('/signup', data={
        'FirstName':'Jane',
        'LastName':'Doe',
        'Email':'janedoe@test.com',
        'PhoneNumber':'1234567890',
        'Password':'password123'
    })
    assert response.status_code in (200, 302)
    assert b'Successfully registered' in response.data
        
def test_login_with_valid_credentials(client):
    """Test login with correct credentials"""
    response = client.post('/login', data={
        'Email':'janedoe@test.com',
        'Password':'password123'
    })
    assert response.status_code in (200, 302)
    assert b'Welcome' in response.data or b'Dashboard' in response.data    
        
def test_login_with_invalid_credentials(client):
    """Test login with wrong password"""
    response.client.post('/login', data={
        'Email':'janedoe@test.com',
        'Password':'wrongpassword789' #Invalid PW
    })
    assert response.status_code == 200
    assert b'Invalid email or password' in response.data
        
def test_invalid_email_format(client):
    """Test signup validation for invalid email"""
    response = client.post('/signup', data={
        'FirstName':'Janis',
        'LastName':'Dope',
        'Email':'wrongemailtype', #Invalid email format
        'PhoneNumber':'1234567890',
        'Password':'password456'
    })
    assert response.status_code == 200
    assert b'Invalid email format' in response.data
        
def test_empty_password_field(client):
    """Test signup validation for empty password"""
    response = client.post('/signup', data={
        'FirstName':'Marco',
        'LastName':'Polo',
        'Email':'marcopolo@test.com', 
        'PhoneNumber':'1234567890',
        'Password':'' #Empty PW field
    })
    assert response.status_code == 200
    assert b'Password is required' in response.data