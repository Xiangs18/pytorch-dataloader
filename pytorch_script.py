import torch
from torch.utils import data

from my_classes import Dataset


# CUDA for PyTorch
use_cuda = torch.cuda.is_available()
device = torch.device("cuda:0" if use_cuda else "cpu")

# Parameters
params = {"batch_size": 1, "shuffle": True, "num_workers": 6}
max_epochs = 5

# Datasets
partition = {"train": ["id-1", "id-2", "id-3"], "validation": ["id-4"]}  # IDs
labels = {"id-1": 0, "id-2": 1, "id-3": 2, "id-4": 1}  # Labels

# Generators
training_set = Dataset(partition["train"], labels)
training_generator = data.DataLoader(training_set, **params)

validation_set = Dataset(partition["validation"], labels)
validation_generator = data.DataLoader(validation_set, **params)

# Loop over epochs
for epoch in range(max_epochs):
    print("--------epoch{}--------".format(epoch))
    print("...Training...")
    for local_batch, local_labels in training_generator:
        # Transfer to GPU
        local_batch, local_labels = local_batch.to(device), local_labels.to(device)

        # Model computations
        # [...]
        print(local_batch.shape, local_labels.shape)

    print("...Validation...")
    with torch.no_grad():
        for local_batch, local_labels in validation_generator:
            # Transfer to GPU
            local_batch, local_labels = local_batch.to(device), local_labels.to(device)

            # Model computations
            # [...]
            print(local_batch.shape, local_labels.shape)
