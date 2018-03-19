class Stock:
    # constructor
    def __init__(
        self, name, num_shares, price, daily_rate, weekly_rate, monthly_rate,
        three_month_rate, yearly_rate, general_rate, dividend):
        self.__name = name
        self.__num_shares = num_shares
        self.__price = price
        self.__daily_rate = daily_rate
        self.__weekly_rate = weekly_rate
        self.__monthly_rate = monthly_rate
        self.__three_month_rate = three_month_rate
        self.__yearly_rate = yearly_rate
        self.__general_rate = general_rate
        self.__dividend = dividend

    # getters and setters
    def get_name(self):
        return self.__name
    def get_num_shares(self):
        return self.__num_shares
    def get_price(self):
        return self.__price
    def get_daily_rate(self):
        return self.__daily_rate
    def get_weekly_rate(self):
        return self.__weekly_rate
    def get_monthly_rate(self):
        return self.__monthly_rate
    def get_three_month_rate(self):
        return self.__three_month_rate
    def get_yearly_rate(self):
        return self.__yearly_rate
    def get_general_rate(self):
        return self.__general_rate
    def get_dividend(self):
        return self.__dividend
    def set_name(self, name):
        self.__name = name
    def set_num_shares(self, num_shares):
        self.__num_shares = num_shares
    def set_price(self, price):
        self.__price = price
    def set_daily_rate(self, daily_rate):
        self.__daily_rate = daily_rate
    def set_weekly_rate(self, weekly_rate):
        self.__weekly_rate = weekly_rate
    def set_monthly_rate(self, monthly_rate):
        self.__monthly_rate = monthly_rate
    def set_three_month_rate(self, three_month_rate):
        self.__three_month_rate = three_month_rate
    def set_yearly_rate(self, yearly_rate):
        self.__yearly_rate = yearly_rate
    def set_general_rate(self, general_rate):
        self.__general_rate = general_rate

