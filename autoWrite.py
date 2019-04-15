import xlrd,xlwt,xlutils
from xlutils.copy import copy


def writeSource(bm):
    stbm = bm.strip()
    if stbm[2:4] != 'DD':
        wr =  '公司'
        return wr
    else:
        return  1
def OpenXlxs():
    readOpenXlsx = xlrd.open_workbook(r"C:\Users\zwl\Desktop\服务接口调用量.xlsx")
    readXlsxSheet = readOpenXlsx.sheet_by_name("Sheet1")
    writeOpenXlsx = copy(readOpenXlsx)

    return readXlsxSheet,writeOpenXlsx



def readXlsx(readXlsxSheet, writeOpenXlsx):
    rowMax = readXlsxSheet.nrows
    colMax = readXlsxSheet.ncols
    for r in range(rowMax):
        if r == 0:
            continue
        else:
            rows = readXlsxSheet.row_values(r)
            print(rows)
            RunValue = readXlsxSheet.cell(r, 0).value
            print(RunValue)
            rsource = writeSource(RunValue)
            writeXlsx(writeOpenXlsx, r,2,r"C:\Users\zwl\Desktop\接口调用量.xlsx",rsource)
#            if RunValue == 'Y':
#                writeXlsx(writeOpenXlsx, r, xlsxName)

def writeXlsx(writeOpenXlsx,row,col,xlsxName,res):
    writeXlsxSheet = writeOpenXlsx.get_sheet(0)
    writeXlsxSheet.write(row,col,res)
    writeOpenXlsx.save(xlsxName)

if __name__ == '__main__':
    readXlsxSheet, writeOpenXlsx = OpenXlxs()
    readXlsx(readXlsxSheet,writeOpenXlsx)
