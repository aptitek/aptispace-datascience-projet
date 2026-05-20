import kagglehub
import os

path = kagglehub.dataset_download(
    "cometx66/house-prices-advanced-regression-techniques"
)

print(path)