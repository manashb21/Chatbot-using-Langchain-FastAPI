#importing settings and get_settings for storing the environment variables in a cache
from config import Settings, get_settings

from dotenv import load_dotenv
load_dotenv(dotenv_path="config/.env")

# to validate API keys coming in through the header
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends

# to return forbidden response and status when APIkey is invalid or not included
from starlette.status import HTTP_403_FORBIDDEN

api_key_header = APIKeyHeader(name="access_token", auto_error=False)
    
async def get_api_key(settings: Settings = Depends(get_settings), api_key_header: str = Security(api_key_header)):
    print(settings)
    if api_key_header == settings.API_KEY:
        return api_key_header   
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )