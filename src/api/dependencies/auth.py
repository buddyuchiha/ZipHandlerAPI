from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from core.auth import keycloak_openid, oauth2_scheme

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Упрощенная проверка через userinfo
    """
    try:
        userinfo = keycloak_openid.userinfo(token)
        print(f"✅ User: {userinfo.get('preferred_username')}")
        return userinfo
    except Exception as e:
        print(f"❌ Auth error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )