import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import FastAPI, Depends, HTTPException,status
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models import TokenTable


# Constants for token expiration times
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days


# Algorithm and secret keys for JWT
ALGORITHM = "HS256"
JWT_SECRET_KEY = "narscbjim@$@&^@&%^&RFghgjvbdsha"   # should be kept secret
# 6937121d28ceb956bc66465684dc42d4f5ac1d717e3badf52cbfcab3894213dc
JWT_REFRESH_SECRET_KEY = "13ugfdfgh@#$%^@&jkl45678902"



# Function to decode the JWT token
def decodeJWT(jwtoken: str):
    try:
        # Decode and verify the token
        payload = jwt.decode(jwtoken, JWT_SECRET_KEY, ALGORITHM)
        return payload
    except InvalidTokenError:
        return None



# Custom class extending HTTPBearer for JWT authentication
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):

        # Get the credentials from the request
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        
        if credentials:
            
            # Check if the authentication scheme is "Bearer"
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            
            # Verify the JWT token
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            
            # Return the token if valid
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            # Decode and verify the token
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        
        # If the payload is not None, the token is valid
        if payload:
            isTokenValid = True
        return isTokenValid


# Create an instance of JWTBearer
jwt_bearer = JWTBearer()
