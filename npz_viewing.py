# import numpy as np

# # Function to inspect the .npz file and print the first few lines of each array
# def inspect_npz(file_path, num_lines=5):
#     # Load the .npz file
#     data = np.load(file_path, allow_pickle=True)
    
#     # List the names of arrays in the .npz file
#     array_names = data.files
#     print("Arrays in the .npz file:", array_names)
    
#     # Print the shape, dtype, and first few lines of each array
#     for name in array_names:
#         print(f"\nArray name: {name}")
#         print("Shape:", data[name].shape)
#         print("Data type:", data[name].dtype)
#         array_content = data[name]
#         # Print the first few lines
#         if array_content.ndim == 1:
#             print(array_content[:num_lines])
#         elif array_content.ndim == 2:
#             print(array_content[:num_lines, :])
#         elif array_content.ndim == 3:
#             print(array_content[:num_lines, :, :])
#         else:
#             print("Array with more than 3 dimensions, displaying the first few elements in the first dimension:")
#             print(array_content[:num_lines])

# # Path to the .npz file
# file_path = "data/PEMS04/pems04.npz"

# # Call the function to inspect the .npz file
# inspect_npz(file_path)

#################################################################
#View individual time slice#
import numpy as np

# Load the .npz file
data = np.load("data/PEMS04/PEMS04_r1_d0_w0_astcgn.npz", allow_pickle=True)

# Access the 'data' array
time_slice = data['data'][1]  # First time slice

# Save the first time slice to a text file
output_path = "second_time_slice.txt"
np.savetxt(output_path, time_slice, fmt='%0.4f', delimiter=', ', header='Second Time Slice of PEMS04 Data')

print(f"Second time slice saved to {output_path}")

############################################################################
# #View how many time slice 
# import numpy as np

# # Load the .npz file
# data = np.load("data/PEMS04/pems04.npz", allow_pickle=True)

# # Access the 'data' array
# traffic_data = data['data']

# # Get the number of time slices
# num_time_slices = traffic_data.shape[0]

# print("Number of time slices in the dataset:", num_time_slices)