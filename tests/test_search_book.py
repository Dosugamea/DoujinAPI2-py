import os
import tempfile

import pytest
from httpx import AsyncClient
from doujinApi.api import DoujinApi


@pytest.mark.asyncio
async def test_search_book_by_name(client: DoujinApi) -> None:
    """
    Test the searchBookByName method of the DoujinApi class.
    """
    resp = await client.searchBookByName("魔法少女は深淵になにをみるか?")
    assert len(resp) == 1


@pytest.mark.asyncio
async def test_search_book_and_get_filename_event_comiket(
    client: DoujinApi,
) -> None:
    """
    Test the parseBookAsFilename method of the DoujinApi class.
    """
    resp = await client.searchBookByName("魔法少女は深淵になにをみるか?")
    filename = client.parseBookAsFilename(resp[0])
    assert filename == "(C89) [こねこぼたん (彩電)] 魔法少女は深淵になにをみるか? (ご注文はうさぎですか?)"


@pytest.mark.asyncio
async def test_search_book_and_get_filename_event_comic_one(
    client: DoujinApi,
) -> None:
    """
    Test the parseBookAsFilename method of the DoujinApi class.
    """
    resp = await client.searchBookByName("ふたりとも、わたしの妹です!")
    filename = client.parseBookAsFilename(resp[0])
    assert filename == "(COMIC1☆17) [こねこぼたん (彩電)] ふたりとも、わたしの妹です! (ご注文はうさぎですか?)"


@pytest.mark.asyncio
async def test_search_book_and_get_filename_event_unknown(
    client: DoujinApi,
) -> None:
    """
    Test the parseBookAsFilename method of the DoujinApi class.
    """
    resp = await client.searchBookByName("悪戯ぎつねと真っ白わんこ")
    filename = client.parseBookAsFilename(resp[0])
    assert filename == "[こねこぼたん (彩電, たそがれ, 天風悠)] 悪戯ぎつねと真っ白わんこ (うらら迷路帖)"


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


@pytest.mark.asyncio
async def test_search_book_by_image(client: DoujinApi) -> None:
    """
    Test the searchBookByImage method of the DoujinApi class.
    """
    fp = tempfile.NamedTemporaryFile(delete=False)
    async with AsyncClient() as http:
        img = await http.get("https://img.doujinshi.org/big/434/868487.jpg")
        fp.write(img.content)
        fp.seek(0)
    resp = await client.searchBookByImage(fp.name)
    fp.close()
    os.unlink(fp.name)
    assert len(resp) > 1
