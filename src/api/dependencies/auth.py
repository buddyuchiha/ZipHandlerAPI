from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from core.auth import keycloak_openid, oauth2_scheme
import requests


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        token_info = keycloak_openid.introspect(token)

        if not token_info.get('active', False):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token is not active"
            )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
        
    return token_info["sub"]