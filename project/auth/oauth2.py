from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from typing import Optional
from datetime import datetime, timedelta
from db.database import get_db
from db.db_user import get_user_by_username
from sqlalchemy.orm import Session
from jose import jwt
from jose.exceptions import JWTError



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '3e7c33c16be13a39a4f27b57c365c4d13ee6bf7857ecdd60dbc5746db27cf575'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def creat_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encoded_jwt



def get_current_user(token: str=Depends(oauth2_scheme), db: Session= Depends(get_db)):
    error_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                     detail='invalid credentials',
                                     headers={'WWW-authenticate':'bearer'})

                                    
try:
    _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    username = _dict.get('sub')
    if not username:
        raise error_credential
except JWTError:
        raise error_credential


user = get_user_by_username(username, db)

return user