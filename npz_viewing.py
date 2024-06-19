import numpy as np

# Function to inspect the .npz file and print the first few lines of each array
def inspect_npz(file_path, num_lines=5):
    # Load the .npz file
    data = np.load(file_path, allow_pickle=True)
    
    # List the names of arrays in the .npz file
    array_names = data.files
    print("Arrays in the .npz file:", array_names)
    
    # Print the shape, dtype, and first few lines of each array
    for name in array_names:
        print(f"\nArray name: {name}")
        print("Shape:", data[name].shape)
        print("Data type:", data[name].dtype)
        array_content = data[name]
        # Print the first few lines
        if array_content.ndim == 1:
            print(array_content[:num_lines])
        elif array_content.ndim == 2:
            print(array_content[:num_lines, :])
        elif array_content.ndim == 3:
            print(array_content[:num_lines, :, :])
        else:
            print("Array with more than 3 dimensions, displaying the first few elements in the first dimension:")
            print(array_content[:num_lines])

# Path to the .npz file
file_path = "data/PEMS04/pems04.npz"

# Call the function to inspect the .npz file
inspect_npz(file_path)

