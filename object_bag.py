# -*- coding: utf-8 -*-

'''
MVC
MVC是分离的,M是模块，V是展示，C是控制器

背包，往里面加东西，取东西，价格
'''


class Model(object):
    
    products = {
        'book':{'price':150,'quantity':10},
        'meat':{'price':20,'quantity':100},
        'cloth':{'price':200,'quantity':10}
    }


class View(object):

    def product_list(self,product_list):
        print ('PRODUCT LIST:')
        for product in product_list:
            print (product)
        print ('')

    def product_information(self,product,product_info):
        print('PRODUCT INFORMATION:')
        print('Name: %s,Price: %.2f,Quantity: %d\n' %
              (product.title(), product_info.get('price',0),
               product_info.get('quantity', 0)))

    def product_not_found(self,product):
        print ('That product "%s" does not exist in the records' %product)


class Controller(object):

    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_product_list(self):
        product_list = self.model.products.keys()
        self.view.product_list(product_list)

    def get_product_information(self,product):
        product_info = self.model.products.get(product, None)
        if product_info is not None:
            self.view.product_information(product,product_info)
        else:
            self.view.product_not_found(product)

#   def set_produnct_information(self,product):
#       self.


if __name__ == '__main__':
    controller = Controller()
    controller.get_product_list()
    controller.get_product_information('book')
    controller.get_product_information('meat')
    controller.get_product_information('cloth')
    controller.get_product_information('computer')
#    controller.set_product_information()




