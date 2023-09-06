# # 모듈
# import theater_module
# theater_module.price(3) # 3명에서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명에서 조조 할인 영화 보러 갔을 때
# theater_module.price_soilder(5) # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv
# mv.price(3) 
# mv.price_morning(4)
# mv.price_soilder(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soilder(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# # price_soilder(7)

from theater_module import price_soilder as ps
ps(5)