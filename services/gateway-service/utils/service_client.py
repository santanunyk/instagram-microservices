import httpx

async def forward_request(method, url, data=None, params=None, headers=None):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method,
            url=url,
            json=data,
            params=params,
            headers=headers
        )
        return response.json()

