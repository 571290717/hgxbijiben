# Day113 Python 与 Excel “大合体”!!! 

[TOC]









> 
>
> Excel是一种常见的电子表格文件格式，广泛用于数据记录和处理。Python提供了多个第三方库，可以方便地对Excel文件进行读写、数据操作和处理。本文将介绍如何使用Python对Excel文件进行处理，并提供相应的代码示例和详细说明。

### 一、安装第三方库

在开始之前，我们需要安装一些Python第三方库，用于对Excel文件进行处理。以下是常用的库：

- pandas：用于数据分析和处理，支持读写Excel文件。
- openpyxl：用于读写Excel文件。
- xlrd：用于读取Excel文件。
- xlwt：用于写入Excel文件。

可以使用pip命令进行安装：

```
pip install pandas openpyxl xlrd xlwt
```

安装完成后，我们可以开始使用这些库来处理Excel文件。

### 二、读取Excel文件

首先，我们需要导入相应的库。使用以下代码导入pandas和openpyxl：

```
import pandas as pd
import openpyxl
```

### 2.1读取Excel文件到DataFrame

使用pandas库可以将Excel文件读取到DataFrame对象中，方便进行数据分析和处理。以下是一个示例代码：

```
# 读取Excel文件
data = pd.read_excel("data.xlsx")

# 打印DataFrame
print(data)
```

这段代码将data.xlsx文件读取到data变量中，并将其打印输出。你可以根据实际文件名和路径进行修改。

### 2.2读取指定Sheet的Excel文件

如果Excel文件中包含多个Sheet，你可以通过指定Sheet名称或索引来读取指定的Sheet。以下是一个示例代码：

```
# 读取指定Sheet的Excel文件
data = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# 打印DataFrame
print(data)
```

这段代码将data.xlsx文件中名为"Sheet1"的Sheet读取到data变量中，并将其打印输出。你可以根据实际情况修改Sheet的名称或使用Sheet的索引。

### 三、写入Excel文件

除了读取Excel文件，我们还可以使用Python将数据写入Excel文件。以下是一个示例代码：

```
# 创建数据
data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'London', 'Paris']
}

# 创建DataFrame
df = pd.DataFrame(data)

# 写入Excel文件
df.to_excel("output.xlsx", index=False)
```

这段代码首先创建了一个包含姓名、年龄和城市的数据字典。然后，通过pd.DataFrame()创建DataFrame对象df。最后，使用to_excel()方法将DataFrame写入到output.xlsx文件中。index=False表示不将索引写入文件。

### 四、修改Excel文件

除了读取和写入，我们还可以使用Python修改Excel文件中的数据、添加新的Sheet等。以下是一个示例代码：

```
# 打开Excel文件
wb = openpyxl.load_workbook("data.xlsx")

# 获取指定Sheet
sheet = wb["Sheet1"]

# 修改单元格数据
sheet["A1"] = "Updated Value"

# 添加新的Sheet
new_sheet = wb.create_sheet("Sheet2")

# 保存修改后的Excel文件
wb.save("data_modified.xlsx")
```

这段代码首先使用openpyxl.load_workbook()方法打开data.xlsx文件，返回一个Workbook对象wb。然后，通过指定Sheet的名称或索引获取指定的Sheet，这里我们获取名为"Sheet1"的Sheet。接下来，我们可以修改Sheet中的单元格数据，例如将"A1"单元格的值修改为"Updated Value"。然后，使用create_sheet()方法添加一个新的Sheet，这里我们创建名为"Sheet2"的Sheet。最后，使用wb.save()方法保存修改后的Excel文件。

### 五、完整代码示例

```
import pandas as pd
import openpyxl

# 读取Excel文件
data = pd.read_excel("data.xlsx")

# 打印DataFrame
print(data)

# 创建数据
data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'London', 'Paris']
}

# 创建DataFrame
df = pd.DataFrame(data)

# 写入Excel文件
df.to_excel("output.xlsx", index=False)

# 打开Excel文件
wb = openpyxl.load_workbook("data.xlsx")

# 获取指定Sheet
sheet = wb["Sheet1"]

# 修改单元格数据
sheet["A1"] = "Updated Value"

# 添加新的Sheet
new_sheet = wb.create_sheet("Sheet2")

# 保存修改后的Excel文件
wb.save("data_modified.xlsx")
```

### 六

# [python处理excel文件(xls格式和xlsx格式)](https://www.cnblogs.com/wolfstark/p/16895823.html)

**一、背景**

帮助客户处理业务员名单, 一万人的名单中处理1700人信息。。。。

 

**二、实现流程：so easy**

1、根据客户提供的待处理人员名单(excel表格)，python脚本读取excel人员信息；

2、脚本获取信息后，再连接数据库，修改这些人员的信息。

 

**三、实现代码: [仅列出处理excel部分脚本]**

**1、说明**

```
"""``Excel中有xls和xlsx两种格式，它们之间的区别是：``  ``1、文件格式不同。xls是一个特有的二进制格式，其核心结构是复合文档类型的结构，<br>　　　　而xlsx的核心结构是XML类型的结构，采用的是基于 XML的压缩方式，使其占用的空间更小。xlsx 中最后一个 x 的意义就在于此。``  ``2、版本不同。xls是Excel2003及以前版本生成的文件格式，而xlsx是Excel2007及以后版本生成的文件格式。``  ``3、兼容性不同。xlsx格式是向下兼容的，可兼容xls格式。` `处理使用的依赖:``  ``xls : [Python自带的模块] 中有针对xls格式的 [xlrd和xlwt] 模块，但这两个库仅仅是针对xls的操作.``  ``xlsx: 当我们要操作xlsx格式文件时，则需要使用到 [openpyxl] 第三方库.``"""


"""
Excel中有xls和xlsx两种格式，它们之间的区别是：
    1、文件格式不同。xls是一个特有的二进制格式，其核心结构是复合文档类型的结构，<br>　　　　而xlsx的核心结构是XML类型的结构，采用的是基于 XML的压缩方式，使其占用的空间更小。xlsx 中最后一个 x 的意义就在于此。
    2、版本不同。xls是Excel2003及以前版本生成的文件格式，而xlsx是Excel2007及以后版本生成的文件格式。
    3、兼容性不同。xlsx格式是向下兼容的，可兼容xls格式。
 
处理使用的依赖:
    xls :  [Python自带的模块] 中有针对xls格式的 [xlrd和xlwt] 模块，但这两个库仅仅是针对xls的操作.
    xlsx:  当我们要操作xlsx格式文件时，则需要使用到 [openpyxl] 第三方库.
"""
```

 

**2、处理xls格式脚本**

（1）安装xlutils依赖

```
pip ``install` `xlutils
```

（2） python处理脚本

```
from` `xlutils.copy ``import` `copy` `import` `xlrd``import` `xlwt` `def` `read_xls_excel(url, index):``  ``'''``  ``读取xls格式文件``  ``参数：``    ``url:文件路径``    ``index：工作表序号（第几个工作表，传入参数从1开始数）``  ``返回：``    ``data:表格中的数据``  ``'''``  ``# 打开指定的工作簿``  ``workbook ``=` `xlrd.open_workbook(url)``  ``# 获取工作簿中的所有表格``  ``sheets ``=` `workbook.sheet_names()``  ``# 获取工作簿中所有表格中的的第 index 个表格``  ``worksheet ``=` `workbook.sheet_by_name(sheets[index``-``1``])``  ``# 定义列表存储表格数据``  ``data ``=` `[]``  ``# 遍历每一行数据``  ``for` `i ``in` `range``(``0``, worksheet.nrows):``    ``# 定义表格存储每一行数据``    ``da ``=` `[]``    ``# 遍历每一列数据``    ``for` `j ``in` `range``(``0``, worksheet.ncols):``      ``# 将行数据存储到da列表``      ``da.append(worksheet.cell_value(i, j))``    ``# 存储每一行数据``    ``data.append(da)``  ``# 返回数据``  ``return` `data` `def` `write_xls_excel(url, sheet_name, two_dimensional_data):``  ``'''``  ``写入xls格式文件``  ``参数：``    ``url:文件路径``    ``sheet_name:表名``    ``two_dimensional_data：将要写入表格的数据（二维列表）``  ``'''``  ``# 创建工作簿对象``  ``workbook ``=` `xlwt.Workbook()``  ``# 创建工作表对象``  ``sheet ``=` `workbook.add_sheet(sheet_name)``  ``# 遍历每一行数据``  ``for` `i ``in` `range``(``0``, ``len``(two_dimensional_data)):``    ``# 遍历每一列数据``    ``for` `j ``in` `range``(``0``, ``len``(two_dimensional_data[i])):``      ``# 写入数据``      ``sheet.write(i, j, two_dimensional_data[i][j])``  ``# 保存``  ``workbook.save(url)``  ``print``(``"写入成功"``)` `def` `write_xls_excel_add(url, two_dimensional_data, index):``  ``'''``  ``追加写入xls格式文件``  ``参数：``    ``url:文件路径``    ``two_dimensional_data：将要写入表格的数据（二维列表）``    ``index：指定要追加的表的序号（第几个工作表，传入参数从1开始数）``  ``'''``  ``# 打开指定的工作簿``  ``workbook ``=` `xlrd.open_workbook(url)``  ``# 获取工作簿中的所有表格``  ``sheets ``=` `workbook.sheet_names()``  ``# 获取指定的表``  ``worksheet ``=` `workbook.sheet_by_name(sheets[index``-``1``])``  ``# 获取表格中已存在的数据的行数``  ``rows_old ``=` `worksheet.nrows` `  ``# 将xlrd对象拷贝转化为xlwt对象``  ``new_workbook ``=` `copy(workbook)``  ``# 获取转化后工作簿中的第index个表格``  ``new_worksheet ``=` `new_workbook.get_sheet(index``-``1``)``  ``# 遍历每一行数据``  ``for` `i ``in` `range``(``0``, ``len``(two_dimensional_data)):``    ``# 遍历每一列数据``    ``for` `j ``in` `range``(``0``, ``len``(two_dimensional_data[i])):``      ``# 追加写入数据，注意是从i+rows_old行开始写入``      ``new_worksheet.write(i``+``rows_old, j, two_dimensional_data[i][j])``  ``# 保存工作簿``  ``new_workbook.save(url)``  ``print``(``"追加写入成功"``)` `if` `__name__ ``=``=` `'__main__'``:``  ``# data = read_xls_excel("/Users/linyiting/Desktop/测试excel文件xls.xls", 2)``  ``# print(data)` `  ``# write_xls_excel(``  ``#   url="/Users/linyiting/Desktop/测试excel文件xls.xls",``  ``#   sheet_name="Sheet2",``  ``#   two_dimensional_data=[["id", "title", "type", "num"], ["1", "战争与和平33", "文学", "100"]])` `  ``write_xls_excel_add(``    ``url``=``"/Users/linyiting/Desktop/测试excel文件xls.xls"``,``    ``two_dimensional_data``=``[[``"id"``, ``"title"``, ``"type"``, ``"num"``], [``"1"``, ``"战争与和平"``, ``"文学"``, ``"100"``]],``    ``index``=``1``)``  ``pass



from xlutils.copy import copy
 
import xlrd
import xlwt
 
 
def read_xls_excel(url, index):
    '''
    读取xls格式文件
    参数：
        url:文件路径
        index：工作表序号（第几个工作表，传入参数从1开始数）
    返回：
        data:表格中的数据
    '''
    # 打开指定的工作簿
    workbook = xlrd.open_workbook(url)
    # 获取工作簿中的所有表格
    sheets = workbook.sheet_names()
    # 获取工作簿中所有表格中的的第 index 个表格
    worksheet = workbook.sheet_by_name(sheets[index-1])
    # 定义列表存储表格数据
    data = []
    # 遍历每一行数据
    for i in range(0, worksheet.nrows):
        # 定义表格存储每一行数据
        da = []
        # 遍历每一列数据
        for j in range(0, worksheet.ncols):
            # 将行数据存储到da列表
            da.append(worksheet.cell_value(i, j))
        # 存储每一行数据
        data.append(da)
    # 返回数据
    return data
 
 
def write_xls_excel(url, sheet_name, two_dimensional_data):
    '''
    写入xls格式文件
    参数：
        url:文件路径
        sheet_name:表名
        two_dimensional_data：将要写入表格的数据（二维列表）
    '''
    # 创建工作簿对象
    workbook = xlwt.Workbook()
    # 创建工作表对象
    sheet = workbook.add_sheet(sheet_name)
    # 遍历每一行数据
    for i in range(0, len(two_dimensional_data)):
        # 遍历每一列数据
        for j in range(0, len(two_dimensional_data[i])):
            # 写入数据
            sheet.write(i, j, two_dimensional_data[i][j])
    # 保存
    workbook.save(url)
    print("写入成功")
 
 
def write_xls_excel_add(url, two_dimensional_data, index):
    '''
    追加写入xls格式文件
    参数：
        url:文件路径
        two_dimensional_data：将要写入表格的数据（二维列表）
        index：指定要追加的表的序号（第几个工作表，传入参数从1开始数）
    '''
    # 打开指定的工作簿
    workbook = xlrd.open_workbook(url)
    # 获取工作簿中的所有表格
    sheets = workbook.sheet_names()
    # 获取指定的表
    worksheet = workbook.sheet_by_name(sheets[index-1])
    # 获取表格中已存在的数据的行数
    rows_old = worksheet.nrows
 
    # 将xlrd对象拷贝转化为xlwt对象
    new_workbook = copy(workbook)
    # 获取转化后工作簿中的第index个表格
    new_worksheet = new_workbook.get_sheet(index-1)
    # 遍历每一行数据
    for i in range(0, len(two_dimensional_data)):
        # 遍历每一列数据
        for j in range(0, len(two_dimensional_data[i])):
            # 追加写入数据，注意是从i+rows_old行开始写入
            new_worksheet.write(i+rows_old, j, two_dimensional_data[i][j])
    # 保存工作簿
    new_workbook.save(url)
    print("追加写入成功")
 
 
if __name__ == '__main__':
    # data = read_xls_excel("/Users/linyiting/Desktop/测试excel文件xls.xls", 2)
    # print(data)
 
    # write_xls_excel(
    #     url="/Users/linyiting/Desktop/测试excel文件xls.xls",
    #     sheet_name="Sheet2",
    #     two_dimensional_data=[["id", "title", "type", "num"], ["1", "战争与和平33", "文学", "100"]])
 
    write_xls_excel_add(
        url="/Users/linyiting/Desktop/测试excel文件xls.xls",
        two_dimensional_data=[["id", "title", "type", "num"], ["1", "战争与和平", "文学", "100"]],
        index=1)
    pass
```

　　

**3、处理xlsx格式脚本**

（1）安装依赖

```
pip ``install` `openpyxl
```

（2）python处理脚本

```
import` `openpyxl` `# 2.2.1. 读取xlsx格式文件``def` `read_xlsx_excel(url, sheet_name):``  ``'''``  ``读取xlsx格式文件``  ``参数：``    ``url:文件路径``    ``sheet_name:表名``  ``返回：``    ``data:表格中的数据``  ``'''``  ``# 使用openpyxl加载指定路径的Excel文件并得到对应的workbook对象``  ``workbook ``=` `openpyxl.load_workbook(url)``  ``# 根据指定表名获取表格并得到对应的sheet对象``  ``sheet ``=` `workbook[sheet_name]``  ``# 定义列表存储表格数据``  ``data ``=` `[]``  ``# 遍历表格的每一行``  ``for` `row ``in` `sheet.rows:``    ``# 定义表格存储每一行数据``    ``da ``=` `[]``    ``# 从每一行中遍历每一个单元格``    ``for` `cell ``in` `row:``      ``# 将行数据存储到da列表``      ``da.append(cell.value)``    ``# 存储每一行数据``    ``data.append(da)``  ``# 返回数据``  ``return` `data` `# 2.2.2. 写入xlsx格式文件``def` `write_xlsx_excel(url, sheet_name, two_dimensional_data):``  ``'''``  ``写入xlsx格式文件``  ``参数：``    ``url:文件路径``    ``sheet_name:表名``    ``two_dimensional_data：将要写入表格的数据（二维列表）``  ``'''``  ``# 创建工作簿对象``  ``workbook ``=` `openpyxl.Workbook()``  ``# 创建工作表对象``  ``sheet ``=` `workbook.active``  ``# 设置该工作表的名字``  ``sheet.title ``=` `sheet_name``  ``# 遍历表格的每一行``  ``for` `i ``in` `range``(``0``, ``len``(two_dimensional_data)):``    ``# 遍历表格的每一列``    ``for` `j ``in` `range``(``0``, ``len``(two_dimensional_data[i])):``      ``# 写入数据（注意openpyxl的行和列是从1开始的，和我们平时的认知是一样的）``      ``sheet.cell(row``=``i ``+` `1``, column``=``j ``+` `1``, value``=``str``(two_dimensional_data[i][j]))``  ``# 保存到指定位置``  ``workbook.save(url)``  ``print``(``"写入成功"``)` `# 2.2.3. 追加写入xlsx格式文件``def` `write_xlsx_excel_add(url, sheet_name, two_dimensional_data):``  ``'''``  ``追加写入xlsx格式文件``  ``参数：``    ``url:文件路径``    ``sheet_name:表名``    ``two_dimensional_data：将要写入表格的数据（二维列表）``  ``'''``  ``# 使用openpyxl加载指定路径的Excel文件并得到对应的workbook对象``  ``workbook ``=` `openpyxl.load_workbook(url)``  ``# 根据指定表名获取表格并得到对应的sheet对象``  ``sheet ``=` `workbook[sheet_name]``  ``for` `tdd ``in` `two_dimensional_data:``    ``sheet.append(tdd)``  ``# 保存到指定位置``  ``workbook.save(url)``  ``print``(``"追加写入成功"``)` `if` `__name__ ``=``=` `'__main__'``:``  ``# data = read_xlsx_excel(``  ``#   url='/Users/linyiting/Desktop/副本提案软件需求文案0906-测试.xlsx',``  ``#   sheet_name='空间配置建议文案'``  ``# )``  ``# print(data)` `  ``write_xlsx_excel_add(``    ``url``=``'/Users/linyiting/Desktop/副本提案软件需求文案0906-测试.xlsx'``,``    ``sheet_name``=``'冰山模型文案'``,``    ``two_dimensional_data``=``[[``"id"``, ``"title"``, ``"type"``, ``"num"``], [``"1"``, ``"战争与和平"``, ``"文学"``, ``"100"``]]``  ``)``  ``pass



import openpyxl
 
 
# 2.2.1. 读取xlsx格式文件
def read_xlsx_excel(url, sheet_name):
    '''
    读取xlsx格式文件
    参数：
        url:文件路径
        sheet_name:表名
    返回：
        data:表格中的数据
    '''
    # 使用openpyxl加载指定路径的Excel文件并得到对应的workbook对象
    workbook = openpyxl.load_workbook(url)
    # 根据指定表名获取表格并得到对应的sheet对象
    sheet = workbook[sheet_name]
    # 定义列表存储表格数据
    data = []
    # 遍历表格的每一行
    for row in sheet.rows:
        # 定义表格存储每一行数据
        da = []
        # 从每一行中遍历每一个单元格
        for cell in row:
            # 将行数据存储到da列表
            da.append(cell.value)
        # 存储每一行数据
        data.append(da)
    # 返回数据
    return data
 
 
# 2.2.2. 写入xlsx格式文件
def write_xlsx_excel(url, sheet_name, two_dimensional_data):
    '''
    写入xlsx格式文件
    参数：
        url:文件路径
        sheet_name:表名
        two_dimensional_data：将要写入表格的数据（二维列表）
    '''
    # 创建工作簿对象
    workbook = openpyxl.Workbook()
    # 创建工作表对象
    sheet = workbook.active
    # 设置该工作表的名字
    sheet.title = sheet_name
    # 遍历表格的每一行
    for i in range(0, len(two_dimensional_data)):
        # 遍历表格的每一列
        for j in range(0, len(two_dimensional_data[i])):
            # 写入数据（注意openpyxl的行和列是从1开始的，和我们平时的认知是一样的）
            sheet.cell(row=i + 1, column=j + 1, value=str(two_dimensional_data[i][j]))
    # 保存到指定位置
    workbook.save(url)
    print("写入成功")
 
 
# 2.2.3. 追加写入xlsx格式文件
def write_xlsx_excel_add(url, sheet_name, two_dimensional_data):
    '''
    追加写入xlsx格式文件
    参数：
        url:文件路径
        sheet_name:表名
        two_dimensional_data：将要写入表格的数据（二维列表）
    '''
    # 使用openpyxl加载指定路径的Excel文件并得到对应的workbook对象
    workbook = openpyxl.load_workbook(url)
    # 根据指定表名获取表格并得到对应的sheet对象
    sheet = workbook[sheet_name]
    for tdd in two_dimensional_data:
        sheet.append(tdd)
    # 保存到指定位置
    workbook.save(url)
    print("追加写入成功")
 
 
if __name__ == '__main__':
    # data = read_xlsx_excel(
    #     url='/Users/linyiting/Desktop/副本提案软件需求文案0906-测试.xlsx',
    #     sheet_name='空间配置建议文案'
    # )
    # print(data)
 
    write_xlsx_excel_add(
        url='/Users/linyiting/Desktop/副本提案软件需求文案0906-测试.xlsx',
        sheet_name='冰山模型文案',
        two_dimensional_data=[["id", "title", "type", "num"], ["1", "战争与和平", "文学", "100"]]
    )
    pass
```

　　

**五、总结**

也没啥可总结的, 文件的IO处理，现成可用，可直接用在项目上，提高效率