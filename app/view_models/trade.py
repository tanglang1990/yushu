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
