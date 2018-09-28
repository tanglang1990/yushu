class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        create_datetime = single.create_datetime
        time = create_datetime.strftime('%Y-%m-%d') if create_datetime else '未知时间'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )


# GiftOrWish 是比较差的命名
# 实际业务中MyTrades可以理解成 MyWishes或者 MyGifts的基类，他们可以继承MyTrades再做自己的小的变动

class MyTrades:
    def __init__(self, trades_of_mine, trade_count_dict):
        self.__trades_of_mine = trades_of_mine
        self.__trade_count_dict = trade_count_dict

        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for gift in self.__trades_of_mine:
            count = self.__trade_count_dict.get(gift.isbn, 0)
            gift = {
                'trades_count': count,
                'book': gift.book,
                'id': gift.id
            }
            temp_trades.append(gift)

        return temp_trades
