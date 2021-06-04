class MobilePhone:
    '''Sample class to illustrate how pyhon classes work'''
    def __init__(self,name, isAndroid = 'False', screen_size = 4.3):
        self.name = name
        self.isAndroid = isAndroid
        self.screen_size = screen_size
        self.rating = -1
    def has_rating(self):
        return self.has_rating > -1

new_phone = MobilePhone('Samsung')
print(type(new_phone))
new_phone.rating = 3.9
print(new_phone.name, new_phone.isAndroid, new_phone.screen_size, new_phone.rating)

