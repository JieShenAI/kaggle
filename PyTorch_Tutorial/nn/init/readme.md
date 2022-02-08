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


# xavier初始化

```python
def xavier(m):
  if type(m) == nn.Linear:
    nn.init.xavier_uniform_(m.weight)

net[0].apply(xavier)
```

对不同的层使用不同的初始化函数

net[1].apply(init_normal)

# weight修改

* `m.weight.data *= m.weight.data.abs() >= 5`

保留m的绝对值大于5的参数，其他的设为0

* 直接修改

所有值加1

`net[0].weight.data[:] + 1`

赋值

`net[0].weight.data[0,0] = 42`
