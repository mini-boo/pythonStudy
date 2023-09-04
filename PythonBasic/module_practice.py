import theater_module

theater_module.price(3) #3명이서 영화보러 갔을 때 가격
theater_module.price_morning(4)
theater_module.price_soldier(2)

import theater_module as mv

mv.price(2)

from theater_module import price, price_morning
price(5)
price_morning(6)

from theater_module import price_soldier as ps
ps(4)