from working_files import generate_files_with_extensions

extensions = ['avi', 'txt', 'mov', 'jpg', 'png', 'mp4', 'gif', 'pdf', 'doc']
num_files_per_extension = [2, 3, 1, 4, 3, 5, 2, 6, 5]
generate_files_with_extensions(extensions, num_files_per_extension)