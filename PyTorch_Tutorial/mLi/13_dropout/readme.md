推理中的丢弃法

* 正则项(dropout)只在训练中使用：它们影响模型参数的更新
* 在推理过程中，丢弃法直接返回输入；(这样保证确定性的输出)

assert 0<a<1

在有dropout情况下，把隐藏层设大一点，把dropout设大一点，效果更好。

丢弃法：
* 在训练时，把神经元丢弃后训练;
* 在预测时，网络中的神经元没有被丢弃;

因为，dropout相当于正则，降低模型的复杂度，所以预测时没有dropout就直接返回输入；

还有一个理由，如果在预测的时候开了dropout，这会导致预测结果波动很大，可能需要训练更多次才能使得它平稳。

dropout参数建议选如下3个值：0.1，0.5，0.9

