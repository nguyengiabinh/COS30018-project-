import numpy as np

# Load the .npz file
# file_path = 'data/PEMS04/pems04.npz'  # Read the unprocessed npz file
# file_path = 'data/PEMS04/PEMS04_r1_d0_w0_astcgn.npz'  # Read the processed npz file
file_path = 'experiments/PEMS04/astgcn_r_h1d0w0_channel1_1.000000e-03/last_predicted_value_epoch_0.npz'
data = np.load(file_path)

# Print the keys (variable names) stored in the .npz file
print("Keys in the .npz file:", data.files)

# Extract and print the contents of each key
for key in data.files:
    print(f"\nData for key '{key}':")
    print(data[key])