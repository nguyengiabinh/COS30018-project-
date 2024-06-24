import numpy as np

# Set print options to ensure all array elements are printed
np.set_printoptions(threshold=np.inf)

# Load the .npz file
npz_file_path = 'data/PEMS04/pems04.npz'
output_file_path = 'npz_content_full.txt'

try:
    npz_file = np.load(npz_file_path, allow_pickle=True)
except FileNotFoundError:
    print(f"File not found: {npz_file_path}")
    exit(1)
except Exception as e:
    print(f"An error occurred while loading the file: {e}")
    exit(1)

# Open a text file to write the output
try:
    with open(output_file_path, 'w') as f:
        # Iterate through each array in the .npz file
        for i, file in enumerate(npz_file.files):
            array_data = npz_file[file]
            f.write(f"Array Name: {file}\n")
            
            # Check the dimensions of the array
            if array_data.ndim == 1 or array_data.ndim == 2:
                np.savetxt(f, array_data, fmt='%s')
            elif array_data.ndim == 3:
                for j in range(array_data.shape[0]):
                    f.write(f"Slice {j}:\n")
                    np.savetxt(f, array_data[j], fmt='%s')
                    f.write("\n")
            else:
                f.write(f"Array with {array_data.ndim} dimensions is not supported for direct saving.\n")
            
            f.write("\n\n")
            f.flush()  # Ensure data is written progressively
            print(f"Written array {i + 1}/{len(npz_file.files)} to file")
        
        # Write the header information
        header_info = {file: {"dtype": npz_file[file].dtype, "shape": npz_file[file].shape} for file in npz_file.files}
        f.write(f"Header Information:\n{header_info}\n")
        f.flush()
        print("Header information written to file")

    print(f"Data successfully written to {output_file_path}")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")






