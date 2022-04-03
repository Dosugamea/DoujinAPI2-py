import xml.etree.ElementTree as etree
from typing import List

from src.book.response import Book
from src.typings.cast import (
    findAndCastBool,
    findAndCastDate,
    findAndCastElementArray,
    findAndCastInt,
    findAndCastLanguage,
    findAndCastOptionalInt,
    findAndCastOptionalStr,
    findAndCastStr,
)
from src.utils.parser import (
    filteredTags,
    parseAuthor,
    parseCharacter,
    parseCircle,
    parseContent,
    parseConvention,
    parseParody,
)


def parseBook(elem: etree.Element) -> Book:
    tags = findAndCastElementArray(elem, "LINKS")
    id = int(elem.attrib["ID"][1:])
    return Book(
        id=elem.attrib["ID"],
        name_jp=findAndCastStr(elem, "NAME_JP"),
        name_en=findAndCastOptionalStr(elem, "NAME_EN"),
        name_r=findAndCastOptionalStr(elem, "NAME_R"),
        circles=[parseCircle(tag) for tag in filteredTags(tags, "circle")],
        authors=[parseAuthor(tag) for tag in filteredTags(tags, "author")],
        characters=[parseCharacter(tag) for tag in filteredTags(tags, "character")],
        parodies=[parseParody(tag) for tag in filteredTags(tags, "parody")],
        contents=[parseContent(tag) for tag in filteredTags(tags, "contents")],
        date_released=findAndCastDate(elem, "DATE_RELEASED"),
        isbn=findAndCastOptionalInt(elem, "DATA_ISBN"),
        pages=findAndCastInt(elem, "DATA_PAGES"),
        nsfw=findAndCastBool(elem, "DATA_AGE"),
        anthology=findAndCastBool(elem, "DATA_ANTHOLOGY"),
        language=findAndCastLanguage(elem, "DATA_LANGUAGE"),
        copyshi=findAndCastBool(elem, "DATA_COPYSHI"),
        magazine=findAndCastBool(elem, "DATA_MAGAZINE"),
        event=[parseConvention(tag) for tag in filteredTags(tags, "convention")][0],
        image=f"https://img.doujinshi.org/big/{int(id/2000)}/{id}.jpg",
        url=f"https://www.doujinshi.org/book/{id}",
    )


def parseBooks(response: etree.Element) -> List[Book]:
    return [parseBook(child) for child in response if child.tag == "BOOK"]
