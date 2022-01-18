# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/1/22 14:26

from torch.utils.data import DataLoader

training_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_dataloader = DataLoader(training_data, batch_size=2, shuffle=True)
# test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)
# print(train_dataloader)
# train_features = next(iter(train_dataloader))


for epoch in range(2):
    for i, data in enumerate(train_dataloader):
        print(i, data)
        # 将数据从 train_loader 中读出来,一次读取的样本数是32个
        # inputs, labels = data
        #
        # # 将这些数据转换成Variable类型
        # inputs, labels = Variable(inputs), Variable(labels)

        # 接下来就是跑模型的环节了，我们这里使用print来代替
        # print("epoch：", epoch, "的第" , i, "个inputs", inputs.data.size(), "labels", labels.data.size())
