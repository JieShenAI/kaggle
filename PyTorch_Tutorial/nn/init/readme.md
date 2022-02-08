torch

nn.init 的一些用法

```python
def init_normal(m):
  if type(m) == nn.Linear:
    nn.init.normal_(n.weight,mean=0.std=0.01)
    nn.init.zeros_(m.bias)

net.apply(init_normal)
net[0].weight.data[0],net[0].bias.data[0]
```

如下只是示范，函数API，不建议这样初始化

把w初始为1

* nn.init.constant_(m.weight,1)

把b初始化为0

* nn.init.zeros_(m.bias)
