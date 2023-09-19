from working_files import generate_files_with_extensions_path

extensions = ['avi', 'txt', 'mov', 'jpg', 'png', 'mp4', 'gif', 'pdf', 'doc']
num_files_per_extension = [2, 3, 1, 4, 3, 5, 2, 6, 5]
directory = 'demo_files'
generate_files_with_extensions_path(extensions, num_files_per_extension, directory)
