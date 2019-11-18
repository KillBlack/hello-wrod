import xlwt,xlrd
from xlutils.copy import copy
def tianjia(hangshu):
    line =0
    xls = xlrd.open_workbook(r'/Users/apple/Desktop/TestUtil/Pythonproject/tete.xls', formatting_info=True)
    xlsc = copy(xls)
    liss = ['swh', 'wym', 'lry', 'hy', 'zdq', 'dl']
    for i in range(100):
        print("这是第" + str(i) + '遍')
        shtc = xlsc.get_sheet(0)
        # shtc.write(2,1,'追加写入的1')
        # shtc.write(2,2,'追加写入的2')
        try:
            shtc.write(hangshu, 0, liss[line], "鸡尾酒")
            print("添加完成")
        except:
            line *= 0
        print(">>>>>>>>>>>")
        shtc.write(hangshu, 1, "华盛顿覅偶")
        print("运行到这里了")
        shtc.write(hangshu, 2, "舅父")
        shtc.write(hangshu, 3, "Jay")
        line += 1
        hangshu += 1
        print(hangshu)
        xlsc.save(r'/Users/apple/Desktop/TestUtil/Pythonproject/tete111.xls')


if __name__ == '__main__':
    tianjia()