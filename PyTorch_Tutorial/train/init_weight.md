```python
def init_weights(m):
  if type(m) == nn.Linear or type(m) == nn.Conv2d:
    nn.init.xavier_uniform(m.weight)
net.apply(init_weights)
```
init_weights函数会遍历net所有的层
