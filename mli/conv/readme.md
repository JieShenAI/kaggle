# conv
卷积等于受限的全连接层，模型复杂度低，相比全连接层很难过拟合

## 输入

1. batch
2. in_channel

卷积输入的第一个维度是batch size,第二个维度是channel;

## conv参数
1. in_channel
2. out_channel
3. kernel: (h,w)

有一点值得注意：kernel参数的数组，第一个维度是out_channel;如果你不能理解，可以查看这张图![image](https://user-images.githubusercontent.com/49408146/153755642-6cadae17-9062-4957-887b-fbd549a9de45.png)


# 卷积核

卷积可以由全连接变形过来

卷积核的大小不是越大越好:

&emsp;这个问题相当于问，MLP中隐藏层的大小不是越大越好。在MLP中窄一点深一点的网络比宽一点浅一点的网络要好。

卷积核，主流是(3,3)，最多是(5,5)

关于卷积核选择，Inception设计思路。不同尺寸的kernel进行计算，计算出一个合适的kernel。

>  1 * 1 的卷积可以实现通道数的降低

# 局部性和平移不变性

卷积核体现局部性；无论目标在哪个地方都是同样的卷积核作用于它体现了**平移不变性**。


# 池化
池化层一般放在卷积层之后，使卷积层对输入不太敏感

池化不做多通道融合，卷积做多通道融合；

池化层的输出通道数 = 输入通道数

> 池化层没有输出通道的超参数

## 种类
* 最大池化层
* 平均池化层

# 特点
PyTorch的池化窗口的大小与步幅大小默认相同，也支持手动设置stride
> 这意味着，下一个池化窗口与上一个池化窗口不会重叠

池化总结
* 池化返回窗口中的最大值或平均值
* 缓解卷积层对位置的敏感性：**通常池化层作用在卷积层之后**
* 同样有窗口的大小、填充和步幅作为超参数
