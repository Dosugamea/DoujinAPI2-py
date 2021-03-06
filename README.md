# DoujinAPI2-py

[Doujinshi.org](https://www.doujinshi.org/) unofficial wrapper of [official API](https://www.doujinshi.org/API_MANUAL.txt)

## Requirements
* Poetry(>=1.16)
* Python(>=3.8.x)
* [Doujinshi.org API KEY](https://www.doujinshi.org/settings/)

## Usage
```bash
pip install doujinapi
or
poetry add doujinapi
```

```python
import asyncio
from doujinApi import DoujinApi

# You can get api key from doujinshi.org easily.
client = DoujinApi("INPUT_YOUR_API_KEY")

async def main():
    searchResult = await client.searchBookByName("魔法少女は深淵になにをみるか?")
    return searchResult

books = asyncio.run(main())
print(books)

# And you'll get below
[Book(
    id='B868487',
    name_jp='魔法少女は深淵になにをみるか?',
    name_en=None,
    name_r=None,
    authors=[Author(
        id='A109490',
        name_jp='彩電',
        name_en=None,
        name_r='None',
        name_alt=[],
        count=47
    )],
    circles=[Circle(
        id='C69210',
        name_jp='こねこぼたん',
        name_en=None,
        name_r='コネコボタン',
        name_alt=[],
        count=41,
        authors=[]
    )],
    parodies=[Parody(
        id='P4828',
        name_jp='ご注文はうさぎですか?',
        name_en='Is the Order a Rabbit?',
        name_r='ゴチュウモンハウサギデスカ',
        name_alt=['Gochūmon wa Usagi Desu ka?',
        'gochuumon wa usagi desu ka'],
        count=1944,
        contents=[],
        characters=[]
    )],
    characters=[
        Character(
            id='H23212',
            name_jp='香風智乃',
            name_en='Kafuu Chino',
            name_r='カフウチノ',
            name_alt=['チノ'],
            count=576,
            sex=<Sex.FEMALE: 2>,
            age=13,
            contents=[]
        ),
        Character(
            id='H23211',
            name_jp='保登心愛',
            name_en='Hoto Kokoa',
            name_r='ホトココア',
            name_alt=[
                'ココア',
                'Cocoa'
            ],
            count=400,
            sex=<Sex.FEMALE: 2>,
            age=None,
            contents=[],
        )
    ],
    contents=[Content(
            name_jp='不詳',
            name_en='Unknown',
            name_r=None,
            count=1601292,
    )],
    date_released=datetime.date(2015, 12, 29),
    event=Convention(
        id='N2386',
        name_jp='コミックマーケット 89',
        name_en='Comic Market 89',
        name_r='コミックマーケット89',
        name_alt=['コミックマーケット89'],
        count=16268,
        date_start=datetime.date(2015,12,29),
        date_end=datetime.date(2015,12,31)
    ),
    image='https://img.doujinshi.org/big/434/868487.jpg',
    url='https://www.doujinshi.org/book/868487',
    pages=28,
    nsfw=False,
    anthology=False,
    copyshi=False,
    magazine=False,
    isbn=None,
    language=<Language.JAPANESE: 3>
)]

# And you can parse the book as filename
filename = client.parseBookAsFilename(books[0])
print(filename)

# And you'll see below
(C89) [こねこぼたん (彩電)] 魔法少女は深淵になにをみるか? (ご注文はうさぎですか?)

# Also you can search book by image
async def main2():
    resp = await client.searchBookByImage("RELATIVE_PATH_TO_IMAGE")
    return resp
```

## Note
Doujinshi.org API is really complex for me.
Please make an issue if something is wrong.

This is rechallenge after 5 years past.
Does this code looks better than [before](https://github.com/Dosugamea/DoujinAPI-py)? XD

Sometimes doujinshi.org server goes down, but don't worry, the server will come back soon :v