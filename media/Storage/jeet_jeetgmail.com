import pandas

df = pandas.read_excel('Student-Sample-Upload.xls')

print df