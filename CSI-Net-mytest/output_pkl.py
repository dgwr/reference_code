# import pickle as pk
# f = open('weights/resnet18_Train100.0Test84.068.pkl', 'rb')
# info = pk.load(f)
# print(info)

import torch

f = open('weights/resnet18_Train100.0Test84.068.pkl','rb')
data = torch.load(f,map_location='cpu')                      #可使用cpu或gpu
print(data)
