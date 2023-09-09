# # # # # 패키지
# # # # import travel.thailand
# # # # trip_to = travel.thailand.ThailandPackage()
# # # # trip_to.detail()

# # # from travel.thailand import ThailandPackage
# # # trip_to = ThailandPackage()
# # # trip_to.detail()

# # from travel import vietnam
# # trip_to = vietnam.Vietnampackage()
# # trip_to.detail()

# from travel import *
# # trip_to = vietnam.Vietnampackage()
# trip_to = thailand.Thailandpackage()
# trip_to.detail()

import inspect
import random
from travel import * 
print(inspect.getfile(random)) # random 모듈이 어느 위치에 있는지 출력
print(inspect.getfile(thailand))
trip_to = thailand.Thailandpackage()
trip_to.detail()