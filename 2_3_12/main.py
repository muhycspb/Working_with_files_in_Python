# Вам дано неопределенное количество файлов трех типов – txt, zip и jpeg, содержащихся в папке structure.
# Определите, сколько файлов txt, zip и jpeg находится в этой папке.
# В файлах типа txt содержится число. Посчитайте сумму всех чисел из этих файлов.
# Ответы запишите в переменные:
# txt_ans – количество файлов типа txt;
# zip_ans – количество файлов типа zip;
# jpeg_ans – количество файлов типа jpeg;
# sum_ans – сумма чисел в текстовых файлах.

from pathlib import Path

sum_ans = 0
txt_ans = len(list(Path.cwd().glob('structure/*.txt')))
zip_ans = len(list(Path.cwd().glob('structure/*.zip')))
jpeg_ans = len(list(Path.cwd().glob('structure/*.jpeg')))

for file in Path.cwd().glob('structure/*.txt'):
    with open(file) as txt_file:
        sum_ans += int(txt_file.read())

# from pathlib import Path
# all_txt_files = [int(i.read_text()) for i in Path.cwd().joinpath('structure').rglob('*.txt')]
# all_zip_files = [_ for _ in Path.cwd().rglob('*.zip')]
# all_jpeg_files = [_ for _ in Path.cwd().rglob('*.jpeg')]
# txt_ans = len(all_txt_files)
# zip_ans = len(all_zip_files)
# jpeg_ans = len(all_jpeg_files)
# sum_ans = sum(all_txt_files)