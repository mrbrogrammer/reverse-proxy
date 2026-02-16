from fastapi import Request, Response

from utils.send_request_utils import send_request_with_body

class UsersRouter:
    def __init__(self):

    # TODO: Read this config from external configurable source

        self.config = {
            "endpoints": {
                "/users": {
                    "methods": ["GET", "POST"],
                    # backend could be load balancer OR a list of backends registered automatically
                    # through a service discovery mechanism
                    "service": "http://localhost:8001" # Load balancing by service
                },
                "/users/{id}": {
                    "methods": ["GET", "POST"],
                    # backend could be load balancer OR a list of backends registered automatically
                    # through a service discovery mechanism
                    "service": "http://localhost:8001" # Load balancing by service
                }
            },
        }

    async def get_user(self, request: Request):
        path = request.path_params["service_url"]
        headers = request.headers.mutablecopy()
        # Send a JWT token from API Header here which backend can validate
        headers["gateway-jwt-token"] = "Some Security Header"
        # Route the request
        print("Routing request to path:", path)
        is_users_path = any(path.startswith(endpoint.split("/")[0]) for endpoint in self.config["endpoints"].keys())
        print("Is users path:", is_users_path)
        
        base_url = self.config["endpoints"][path]["service"] + path

        return await send_request_with_body(
            method=request.method,
            service_url=base_url,
            headers=headers,
            query_params=request.query_params,
            body=await request.body()
        )
