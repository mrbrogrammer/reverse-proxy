from exception.RouterNotFoundException import RouterNotFoundException
from fastapi import Request, Response

from aiohttp import ClientSession


async def send_request_with_body(method, service_url, headers, query_params, body):
    
    async with ClientSession() as client:
        try:
            # Forward the request to the target service
            # response = await client.request(
            #     method,
            #     service_url,
            #     headers=headers,
            #     params=query_params,
            #     content=body
            # )
            response = await client.get(url=service_url, headers=headers)
            data = await response.content.read()
            modified_headers = response.headers.copy()
            add_headers(modified_headers)

            # Return the response from the backend service
            return Response(content=data, status_code=response.status, headers=modified_headers)

        except Exception as exc:
            raise RouterNotFoundException(500, detail=f"Backend service request error: {exc}")

def add_headers(modified_headers):
    # OWASP Secure Headers https://owasp.org/www-project-secure-headers/
    modified_headers['X-XSS-Protection'] = '1; mode=block'
    modified_headers['X-Frame-Options'] = 'DENY'
    modified_headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
    modified_headers['X-Content-Type-Options'] = 'nosniff'

    # Avoid Caching Tokens
    modified_headers['Expires'] = '0'
    modified_headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    modified_headers['Pragma'] = 'no-cache'