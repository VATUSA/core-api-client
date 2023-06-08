import logging
import os
from typing import Optional

import aiohttp
import pydantic
from vatusa_core.config import APIConfig


log = logging.getLogger('vatusa_core')


def get_session():
    if APIConfig.url is None:
        raise Exception("Attempt to create api session without APIConfig.url set")
    if APIConfig.token is None:
        raise Exception("Attempt to create api session without APIConfig.token set")

    return aiohttp.ClientSession(
        base_url=APIConfig.url,
        headers={'Authorization': f'Token {APIConfig.token}'}
    )


async def get(uri: str):
    if not uri.startswith('/'):
        raise Exception("Malformed URI - Must start with /")
    async with get_session() as session:
        async with session.get(uri) as resp:
            log.debug(f'Response from GET {uri} - HTTP {resp.status}')
            return await resp.json()


async def post(uri: str, data: pydantic.BaseModel):
    if not uri.startswith('/'):
        raise Exception("Malformed URI - Must start with /")
    async with get_session() as session:
        async with session.post(uri, json=data.dict()) as resp:
            log.debug(f'Response from POST {uri} - HTTP {resp.status}')
            return await resp.json()


async def put(uri: str, data: pydantic.BaseModel):
    if not uri.startswith('/'):
        raise Exception("Malformed URI - Must start with /")
    async with get_session() as session:
        async with session.put(uri, json=data.dict()) as resp:
            log.debug(f'Response from PUT {uri} - HTTP {resp.status}')
            return await resp.json()


async def patch(uri: str, data: pydantic.BaseModel):
    if not uri.startswith('/'):
        raise Exception("Malformed URI - Must start with /")
    async with get_session() as session:
        async with session.patch(uri, json=data.dict()) as resp:
            log.debug(f'Response from PATCH {uri} - HTTP {resp.status}')
            return await resp.json()


async def delete(uri: str):
    if not uri.startswith('/'):
        raise Exception("Malformed URI - Must start with /")
    async with get_session() as session:
        async with session.delete(uri) as resp:
            log.debug(f'Response from DELETE {uri} - HTTP {resp.status}')
            return await resp.json()
