# from collections import namedtuple

# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_dict):
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_dict = wish_count_dict
        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            count = self.__wish_count_dict.get(gift.isbn, 0)
            gift = {
                'wishes_count': count,
                'book': gift.book,
                'id': gift.id
            }
            temp_gifts.append(gift)
            # gift = MyGift(count, gift.book, gift.id)
            # temp_gifts.append(gift)

        return temp_gifts
