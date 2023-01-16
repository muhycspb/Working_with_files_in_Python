# Напишите программу, которая поместит в zip архив папку files. Назовите его archive.
#
# Как протестировать ваше решение?
# Создайте в отдельной папке файл main.py.
# В этой папке создайте папку files.
# Создайте в папке files несколько файлов типа txt.
# Напишите программу, решающую поставленную задачу.
# Проверьте, что все работает, запустив программу.
# Измените количество файлов txt и проверьте, что все корректно.

import shutil

shutil.make_archive('archive', 'zip', 'files')
