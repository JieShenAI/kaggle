## net struct

```python
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
```



```python
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
```

flatten，展平

```python
flatten = nn.Flatten()
flat_image = flatten(input_image)
print(flat_image.size())
```

activation function

```python
pred_probab = nn.Softmax(dim=1)(logits)
```

`nn.Sequential <https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html>`_ is an ordered container of modules. The data is passed through all the modules in the same order as defined. You can use sequential containers to put together a quick network like `seq_modules`.

```python
flatten = nn.Flatten()
layer1 = nn.Linear(in_features=28*28, out_features=20)
seq_modules = nn.Sequential(
    flatten,
    layer1,
    nn.ReLU(),
    nn.Linear(20, 10)
)
input_image = torch.rand(3,28,28)
logits = seq_modules(input_image)
softmax = nn.Softmax(dim=1)
pred_probab = softmax(logits)
```

## show parameters

```python
print("Model structure: ", model, "\n\n")

for name, param in model.named_parameters():
    print(f"Layer: {name} | Size: {param.size()} | Values : {param[:2]} \n")
```



Model structure:  

NeuralNetwork(  (flatten): Flatten(start_dim=1, end_dim=-1)  (linear_relu_stack): 

Sequential(    

(0): Linear(in_features=784, out_features=512, bias=True)    

(1): ReLU()   

(2): Linear(in_features=512, out_features=512, bias=True)    

(3): ReLU()    

(4): Linear(in_features=512, out_features=10, bias=True)  ) ) 



Layer: linear_relu_stack.0.weight | Size: torch.Size(**[512, 784]**) | Values : tensor([[-0.0089,  0.0275, -0.0199,  ..., -0.0226,  0.0053, -0.0267],        [ 0.0094,  0.0019, -0.0281,  ...,  0.0211,  0.0327, -0.0325]],       grad_fn=<SliceBackward0>)  

Layer: linear_relu_stack.0.bias | Size: torch.Size([512]) | Values : tensor([-0.0250,  0.0178], grad_fn=<SliceBackward0>)  

Layer: linear_relu_stack.2.weight | Size: torch.Size(**[512, 512]**) | Values : tensor([[-0.0239,  0.0151,  0.0347,  ..., -0.0077,  0.0134, -0.0136],        [-0.0172,  0.0031, -0.0096,  ...,  0.0079,  0.0373,  0.0007]],       grad_fn=<SliceBackward0>)  

Layer: linear_relu_stack.2.bias | Size: torch.Size([512]) | Values : tensor([ 0.0307, -0.0098], grad_fn=<SliceBackward0>)  

Layer: linear_relu_stack.4.weight | Size: torch.Size(**[10, 512]**) | Values : tensor([[ 0.0076,  0.0161, -0.0149,  ..., -0.0205,  0.0108, -0.0004],        [ 0.0135,  0.0261, -0.0134,  ..., -0.0176, -0.0307, -0.0182]],       grad_fn=<SliceBackward0>)  

ayer: linear_relu_stack.4.bias | Size: torch.Size([10]) | Values : tensor([-0.0419, -0.0018], grad_fn=<SliceBackward0>) 



注意上面加粗的字体可以发现，torch参数与在net struct定义的是相反的。

