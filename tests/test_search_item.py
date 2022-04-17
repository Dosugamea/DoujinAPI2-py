import pytest
from doujinApi.api import DoujinApi


@pytest.mark.asyncio
async def test_search_circle_by_name(client: DoujinApi) -> None:
    """
    Test the searchCircleByName method of the DoujinApi class.
    """
    resp = await client.searchCircleByName("こねこボタン")
    assert len(resp) == 1


@pytest.mark.asyncio
async def test_search_author_by_name(client: DoujinApi) -> None:
    """
    Test the searchAuthorByName method of the DoujinApi class.
    """
    resp = await client.searchAuthorByName("彩電")
    assert len(resp) == 1


@pytest.mark.asyncio
async def test_search_parody_by_name(client: DoujinApi) -> None:
    """
    Test the searchParodyByName method of the DoujinApi class.
    """
    resp = await client.searchParodyByName("ご注文はうさぎですか?")
    assert len(resp) == 1


@pytest.mark.asyncio
async def test_search_character_by_name(client: DoujinApi) -> None:
    """
    Test the searchCharacterByName method of the DoujinApi class.
    """
    resp = await client.searchCharacterByName("香風智乃")
    assert len(resp) == 1


@pytest.mark.asyncio
async def test_search_tag_by_name(client: DoujinApi) -> None:
    """
    Test the searchTagByName method of the DoujinApi class.
    """
    resp = await client.searchTagByName("ロリ")
    assert len(resp) > 1
