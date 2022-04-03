import pytest
from src.api import DoujinApi


@pytest.mark.asyncio
async def test_search_book_by_name(client: DoujinApi) -> None:
    """
    Test the searchBookByName method of the DoujinApi class.
    """
    resp = await client.searchBookByName("魔法少女は深淵になにをみるか?")
    assert len(resp) == 1


@pytest.mark.asyncio
async def test_search_book_by_circle(client: DoujinApi) -> None:
    """
    Test the searchBookByCircle method of the DoujinApi class.
    """
    resp = await client.searchBookByCircle("こねこぼたん")
    assert len(resp) > 1


@pytest.mark.asyncio
async def test_search_book_by_author(client: DoujinApi) -> None:
    """
    Test the searchBookByAuthor method of the DoujinApi class.
    """
    resp = await client.searchBookByAuthor("彩電")
    assert len(resp) > 1


@pytest.mark.asyncio
async def test_search_book_by_parody(client: DoujinApi) -> None:
    """
    Test the searchBookByParody method of the DoujinApi class.
    """
    resp = await client.searchBookByParody("ご注文はうさぎですか?")
    assert len(resp) > 1


@pytest.mark.asyncio
async def test_search_book_by_character(client: DoujinApi) -> None:
    """
    Test the searchBookByCharacter method of the DoujinApi class.
    """
    resp = await client.searchBookByCharacter("香風智乃")
    assert len(resp) > 1


@pytest.mark.asyncio
async def test_search_book_by_tag(client: DoujinApi) -> None:
    """
    Test the searchBookByTag method of the DoujinApi class.
    """
    resp = await client.searchBookByTag("ロリ")
    assert len(resp) > 1