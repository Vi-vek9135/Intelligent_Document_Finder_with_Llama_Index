import os
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt



# Constants for token expiration times
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days


# Algorithm and secret keys for JWT
ALGORITHM = "HS256"
JWT_SECRET_KEY = "narscbjim@$@&^@&%^&RFghgjvbdsha"   # should be kept secret
JWT_REFRESH_SECRET_KEY = "13ugfdfgh@#$%^@&jkl45678902"


# Creating a CryptContext instance with bcrypt scheme
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:

    """
    Hashes the provided password using bcrypt.

    Args:
        password (str): The plaintext password to be hashed.

    Returns:
        str: The hashed password.
    """


    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    
    """
    Verifies the provided password against the hashed password.

    Args:
        password (str): The plaintext password to verify.
        hashed_pass (str): The hashed password to compare against.

    Returns:
        bool: True if the password matches the hashed password, False otherwise.
    """
    
    
    return password_context.verify(password, hashed_pass)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    
    """
    Creates an access token using JWT.

    Args:
        subject (Union[str, Any]): The subject or data to be encoded in the token.
        expires_delta (int, optional): The number of minutes until the token expires. Defaults to ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns:
        str: The encoded access token.
    """
    
    
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
        
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
         
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
     
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    
    """
    Creates a refresh token using JWT.

    Args:
        subject (Union[str, Any]): The subject or data to be encoded in the token.
        expires_delta (int, optional): The number of minutes until the token expires. Defaults to REFRESH_TOKEN_EXPIRE_MINUTES.

    Returns:
        str: The encoded refresh token.
    """
    
    
    
    
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
