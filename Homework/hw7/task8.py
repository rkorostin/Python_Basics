import os

from working_files import rename_files

# перед запуском запустить task4.py (это для генерации файлов)
os.chdir('demo_files')
rename_files("_new", 3, ".txt", ".docx", [3, 5])
