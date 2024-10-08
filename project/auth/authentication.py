from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestFrom
from sqlalchemy.orm.session import Session
from db import models
from db.database import get_db
from db.hash import Hash
from auth import oauth2


router = APIRouter(tags=['authentication'])


@router.post('/token')
def get_token(request: OAuth2PasswordRequestFrom=Depends(), db: Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid password')


    access_token = oauth2.creat_access_token(data={'sub': request.username})


    return {
        'access_token': access_token,
        'type_token': 'bearer',
        'userID': user.id,
        'username': user.username
    }