# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/1/18 20:13
import torchvision

from com.jieshen.JTorch import *

# # As a car company we collect this data from previous selling
# # lets define car prices
# car_prices_array = [3, 4, 5, 6, 7, 8, 9]
# car_price_np = np.array(car_prices_array, dtype=np.float32)
# car_price_np = car_price_np.reshape(-1, 1)
# car_price_tensor = Variable(torch.from_numpy(car_price_np))
#
# # lets define number of car sell
# number_of_car_sell_array = [7.5, 7, 6.5, 6.0, 5.5, 5.0, 4.5]
# number_of_car_sell_np = np.array(number_of_car_sell_array, dtype=np.float32)
# number_of_car_sell_np = number_of_car_sell_np.reshape(-1, 1)
# number_of_car_sell_tensor = Variable(torch.from_numpy(number_of_car_sell_np))
#
# # lets visualize our data
# import matplotlib.pyplot as plt
#
# plt.scatter(car_prices_array, number_of_car_sell_array)
# plt.xlabel("Car Price $")
# plt.ylabel("Number of Car Sell")
# plt.title("Car Price$ VS Number of Car Sell")
# plt.show()


torchvision.datasets.mnist.FashionMNIST