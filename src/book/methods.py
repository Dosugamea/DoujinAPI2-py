from typing import List, Optional

from src.book.parser import parseBooks
from src.book.request import SearchBookRequest, SearchBookRequestFilter
from src.book.response import Book
from src.utils.session import Session


class SearchBookMethods(Session):
    def __init__(self, apiKey: str) -> None:
        Session.__init__(self, apiKey)

    async def __search(
        self,
        keyword: Optional[str] = None,
        filter: Optional[SearchBookRequestFilter] = None,
        page: int = 1,
    ) -> List[Book]:
        req = SearchBookRequest(S="objectSearch", page=page)
        if keyword:
            req["sn"] = keyword
        if filter:
            req["slist"] = str(filter)
        resp = await self.get(req)
        return parseBooks(resp)

    async def searchBook(
        self,
        request: SearchBookRequestFilter,
        keyword: Optional[str] = None,
        page: int = 1,
    ) -> List[Book]:
        return await self.__search(keyword, request, page)

    async def searchBookByName(self, title: str, page: int = 1) -> List[Book]:
        return await self.__search(title, None, page)

    async def searchBookByCircle(self, title: str, page: int = 1) -> List[Book]:
        filter = SearchBookRequestFilter().circle(title)
        return await self.__search(None, filter, page)

    async def searchBookByAuthor(self, title: str, page: int = 1) -> List[Book]:
        filter = SearchBookRequestFilter().author(title)
        return await self.__search(None, filter, page)

    async def searchBookByParody(self, title: str, page: int = 1) -> List[Book]:
        filter = SearchBookRequestFilter().parody(title)
        return await self.__search(None, filter, page)

    async def searchBookByCharacter(self, title: str, page: int = 1) -> List[Book]:
        filter = SearchBookRequestFilter().character(title)
        return await self.__search(None, filter, page)

    async def searchBookByTag(self, title: str, page: int = 1) -> List[Book]:
        filter = SearchBookRequestFilter().tag(title)
        return await self.__search(None, filter, page)
