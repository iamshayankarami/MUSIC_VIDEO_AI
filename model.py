import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

n_hidden = 128

class NN(nn.Module):
	def __init__(self, in_channel, out_channel, hidden_size):
		super(NN, self).__init__()
		self.hidden_size = hidden_size
		self.i2h = nn.Linear(in_channel + hidden, hidden)
		self.i2o = nn.Linear(in_channel + hidden, out_channel)
		self.softmax = nn.LogSoftmax(dim=1)
	def forward(self, input, hidden):
		combined = torch.cat((input, hidden), 1)
		hidden = self.i2h(combined)
		output = self.i2o(combined)
		output = softmax(output)
		return output, hidden
	def inithidden(self):
		return torch.zeros(1, self.hidden_size)

Model = NN(len(data), len(edjs), n_hidden)

