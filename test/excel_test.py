import xlwt
import xlrd
import xlutils

# # 写excel
# book=xlwt.Workbook()
# sheet=book.add_sheet('sheet1')
# # sheet.write(0,0,'id')  #指定行和列内容
# # sheet.write(0,1,'username')
# # sheet.write(0,2,'password')
# #
# # sheet.write(1,0,'1')
# # sheet.write(1,1,'niuhanyang')
# # sheet.write(1,2,'123456')
#
# stus=[
#     [1,'njf','1234'],
#     [2,'njf1','1234'],
#     [3,'njf2','1234'],
#     [4,'njf3','1234'],
#     [5,'njf4','1234'],
#     [6,'njf5','1234'],
#     [7,'njf6','1234'],
#     [8,'njf7','1234'],
#     [9,'njf8','1234'],
#     [10,'njf9','1234'],
# ]
# line=0  #控制的是行
# for stu in stus:
#     col=0
#     for s in stu:
#         sheet.write(line,col,s)
#         col+=1
#     line+=1
#
# book.save('stu.xls')
#


import xlrd

book=xlrd.open_workbook('stu.xls')
sheet=book.sheet_by_index(0)  #根据sheet编号来
# sheet=book.sheet_by_name('sheet1')   #根据 sheet名称来
print(sheet.nrows)  #excel里面有多少行
print(sheet.ncols)  #excel里面有多少列
print(sheet.cell(0,0).value)  #获取第0行第0列的值
print(sheet.row_values(0))  #获取到整行的内容
print(sheet.col_values(0)) #获取到整列的内容

for i in range(sheet.nrows):  #循环获取每行的内容
    print(sheet.row_values(i))