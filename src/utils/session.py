import xml.etree.ElementTree as etree
from typing import Union

from httpx import AsyncClient
from src.book.request import SearchBookRequest
from src.item.request import SearchItemRequest
from src.utils.exception import UnauthorizedException


class Session(object):
    ENDPOINT = "https://www.doujinshi.org/api"
    API_KEY = ""

    def __init__(self, apiKey: str) -> None:
        self.API_KEY = apiKey

    async def get(
        self, params: Union[SearchBookRequest, SearchItemRequest]
    ) -> etree.Element:
        async with AsyncClient() as client:
            params_dict: dict = params  # type: ignore
            resp = await client.get(
                f"{self.ENDPOINT}/{self.API_KEY}/", params=params_dict
            )
            tree = etree.fromstring(resp.text.encode("utf-8"))
            for child in tree:
                if child.tag == "ERROR":
                    if child.attrib["code"] == "1":
                        raise UnauthorizedException("Wrong API Key")
            return tree
