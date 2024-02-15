from pprint import pprint
from typing import Optional
import aiohttp
from .exceptions import NotFound, StoreLeadsAPIError
from .models.domain import DomainInfo
from .models.app import App
from .types import GeneralDict


class APIClient:
    def __init__(self, api_key: str, api_version: int = 1) -> None:
        self.api_key = api_key
        self.api_version = api_version
        self._base_url = f"https://storeleads.app/json/api/v{self.api_version}/all"
        self._session = aiohttp.ClientSession()

    def get_headers(self, headers: Optional[GeneralDict] = None) -> GeneralDict:
        if not headers:
            headers = {"Authorization": f"Bearer {self.api_key}"}

        return headers

    async def _request(
        self,
        method: str,
        path: str,
        data: GeneralDict | str | bytes,
        headers: Optional[GeneralDict] = None,
    ) -> GeneralDict:
        url = self._base_url + path

        if isinstance(data, str):
            data = data.encode("utf-8")

        headers = self.get_headers()

        async with self._session.request(
            method=method, url=url, headers=headers, data={}
        ) as resp:
            await resp.read()

        try:
            r = await resp.json()
            if "error" in r.keys():
                raise StoreLeadsAPIError(r)

            return r

        except aiohttp.ContentTypeError:
            raise StoreLeadsAPIError(await resp.text())

    async def retrieve_an_app(self, domain: str) -> App:
        path = f"/app/{domain}"
        resp = await self._request("GET", path, data={})
        print(resp)

        return App(resp["app"])

    async def get_domain_info(self, domain: str) -> DomainInfo:
        path = f"/domain/{domain}"
        resp = await self._request("GET", path, data={})

        pprint(resp["domain"])

        return DomainInfo(resp["domain"])
        print(resp)
        for d in resp["domain"]:
            domain_info = DomainInfo(d)

            if domain_info.name == domain:
                return domain_info

        else:
            raise NotFound(resp)
