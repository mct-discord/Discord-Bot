import requests
from quart import request, Request, Response
    
class ADAuth:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if "headers" not in scope or scope['method'] == 'OPTIONS':
            return await self.app(scope, receive, send)

        for header, value in scope['headers']:
            if header.decode('utf-8') == 'authorization':
                auth = value.decode('utf-8').split(' ')[1];
                try:
                    response = requests.post('https://mctdiscord.azurewebsites.net/.auth/login/aad',json={'access_token': auth})
                    if response.status_code == 200:
                        return await self.app(scope, receive, send)
                except Exception as ex:
                    print(ex)
                

        return await self.error_response(receive, send)

    async def error_response(self, receive, send):
        await send({
            'type': 'http.response.start',
            'status': 401,
            'headers': [(b'content-length', b'0')],
        })
        await send({
            'type': 'http.response.body',
            'body': b'',
            'more_body': False,
        })

