from src.book.methods import SearchBookMethods
from src.item.methods import SearchItemMethods


class DoujinApi(SearchItemMethods, SearchBookMethods):
    def __init__(self, apiKey: str) -> None:
        SearchItemMethods.__init__(self, apiKey)
        SearchBookMethods.__init__(self, apiKey)
