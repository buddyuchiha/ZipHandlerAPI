from fastapi.security import HTTPBearer, OAuth2AuthorizationCodeBearer
from keycloak import KeycloakOpenID

from core.config import settings


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{settings.get_kc_url()}/realms/"
                     f"{settings.KC_REALM}/protocol/openid-connect/auth",
    tokenUrl=f"{settings.get_kc_url()}/realms/"
             f"{settings.KC_REALM}/protocol/openid-connect/token",
)

keycloak_openid = KeycloakOpenID(
    server_url=settings.get_kc_url(),
    realm_name=settings.KC_REALM,
    client_id=settings.KC_CLIENT_ID,
    client_secret_key=settings.KC_CLIENT_SECRET,
    verify=True
)

security = HTTPBearer()