import torch
# use cpu or gpu based on your system
device = "cpu"
if torch.cuda.is_available():
    device = "cuda"

# convert our text data into tokenized tensor
data_dir = "1/data.txt"
text = open(data_dir, 'r').read() 

chars = list(set(text))
vocab_size = len(chars)

chr_to_idx = {c:i for i, c in enumerate(chars)}
idx_to_chr = {i:c for i, c in enumerate(chars)}

def encode(input_text: str) -> list[int]:
    return [chr_to_idx[t] for t in input_text]

def decode(input_tokens: list[int]) -> str:
    return "".join([idx_to_chr[i] for i in input_tokens])


data = torch.tensor(encode(text), dtyppe=torch.long, device=device)
