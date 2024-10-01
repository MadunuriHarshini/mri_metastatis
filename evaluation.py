from torch.utils.data import DataLoader
from torch.optim import Adam
import torch.nn.functional as F
import torch

# Assume you have implemented a custom Dataset class for MRI images and masks

# DataLoader
train_loader = DataLoader(dataset=train_dataset, batch_size=4, shuffle=True)
val_loader = DataLoader(dataset=val_dataset, batch_size=4, shuffle=False)

# Training function
def train_model(model, train_loader, val_loader, num_epochs=25):
    optimizer = Adam(model.parameters(), lr=1e-4)
    for epoch in range(num_epochs):
        model.train()
        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = F.binary_cross_entropy_with_logits(outputs, targets)
            loss.backward()
            optimizer.step()

        # Validation
        model.eval()
        dice_score = 0
        with torch.no_grad():
            for inputs, targets in val_loader:
                outputs = model(inputs)
                dice_score += calculate_dice_score(outputs, targets)

        print(f"Epoch {epoch+1}, DICE Score: {dice_score/len(val_loader)}")

# Train Nested U-Net and Attention U-Net
train_model(nested_unet, train_loader, val_loader)
