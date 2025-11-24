from keycloak import KeycloakOpenID
from fastapi.security import HTTPBearer, OAuth2AuthorizationCodeBearer

keycloak_server_url = "http://localhost:9090"
realm_name = "zip-checker"

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{keycloak_server_url}/realms/{realm_name}/protocol/openid-connect/auth",
    tokenUrl=f"{keycloak_server_url}/realms/{realm_name}/protocol/openid-connect/token",
)

keycloak_openid = KeycloakOpenID(
    server_url=keycloak_server_url,
    realm_name=realm_name,
    client_id="zip-service",
    client_secret_key="fixed-client-secret-for-dev",
    verify=True
)
security = HTTPBearer()