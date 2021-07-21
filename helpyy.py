# for i in range(0,100,11):
#     print(i)
# s = '1'
# #####234321
# print(s[-2::-1])
# lst = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,101,111,121,131,141,151,161,171,181,191,202,212,222,232,242,252,262,272,282,292,303,313,323,333,343,353,363,373,383,393,404,414,424,434,444,454,464,474,484,494,505,515]
# for i in lst:
#     if str(i**2) == str(i**2)[::-1]:
#         print(i,i**2)
# print(10**((len('10000'))/2))
class Product(object):
    deliveryCharge = 50
    def __init__(self, nam, prc):
        self.name = nam
        self.price = prc

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price + self.deliveryCharge

    def __str__(self):
        return 'The {} will cost you Rs.{}'.format(self.get_name(), self.get_price())

class Gift(Product):
    wrapping_charge = 100
    def __init__(self,nam,prc):
        Product.__init__(self,nam,prc)
    def get_price(self):
        return self.price + self.deliveryCharge + self.wrapping_charge

if __name__ == '__main__':
    toy = Gift('barbie',300)
    print(toy.get_price())
    print(str(toy))
# class A(object):
#      def __init__(self,x=0,y=0):
#          self.x = x
#          self.y = y
#          # print('hi',self.x,self.y)
#
# class B(A):
#     def __init__(self,x,y):
#         A.__init__(self,x,y)
#     def dis(self):
#         return["hello", self.x, self.y]
#
# b= B('ji',2)
# print(b.dis())