SSD代码

[SSD mLi 代码实现 bilibili](https://www.bilibili.com/video/BV1ZX4y1c7Sw?p=2)

[SSD d2l教材](https://zh-v2.d2l.ai/chapter_computer-vision/ssd.html)

1. nn.Conv2D [eg](https://github.com/JieShenAI/kaggle/blob/main/mli/19_conv/Conv2d.ipynb)


7.3节一节介绍的使用卷积层的通道来输出类别预测的方法， 单发多框检测采用同样的方法来降低模型复杂度。


#　遗留的问题

* 如何从众多的模框中，选出最合适的模框
* 如何确定是哪个像素和它的边界框
