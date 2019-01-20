import torch

# a=[[1,2],[3,4],[4,5]]
# # a=[3.]
#
# a = torch.cuda.FloatTensor(a)
#
# b = a**2
# print(a,'\n',b,'\n')

x = torch.tensor([[11., -112.], [11., 11.]], requires_grad=True)
out = x.pow(2).sum()
print(out)
out.backward()
print(x.grad)