## python 格式化输出详解（占位符：%、format、f表达式）——下篇 示例篇

### 格式化输出内容为markdown表格格式 —— 使用f表达式
markdown表格语法如下
```markdown
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |
```
其表现效果则为

|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |


#### 详情描述：
有表头内容和单元格内容，均为列表，要输出成markdwon语法格式，同时希望输出内容本身能够尽可能对齐。


补充：中文对齐，尝试使用两格位置来对其，如果中文占位不是两格则对不起。

由于每个内容的对齐长度是存放在变量里的，所以这个场景最适合使用f表达式。

代码如下：
```python
# require: python3.6 or above
def count_width(s, align_zh):
    s = str(s)

    count = 0
    for ch in s:
        if align_zh and u'\u4e00' <= ch <= u'\u9fff':  # 中文占两格
            count += 2
        else:
            count += 1

    return count


def print_to_markdwon_table(column, rows, align_zh = False):

    widths = []
    column_str = ""
    separate = "----"
    separate_str = ""
    # 计算每一列的宽度：最长字段
    for ci, cname  in enumerate(column):
        cw = count_width(cname, align_zh)
        for row in rows:
            item = row[ci]

            if count_width(item, align_zh) > cw:
                cw = count_width(item, align_zh)

        widths.append(cw)

        delete_count = count_width(cname, align_zh) - count_width(cname, False)

        column_str += f'|{cname:^{cw-delete_count+2}}'
        separate_str += f'|{separate:^{cw+2}}'

    column_str += "|"
    separate_str += "|"

    print(column_str)
    print(separate_str)

    for ri, row in enumerate(rows):
        row_str = ""
        for ci, item in enumerate(row):
            cw = widths[ci]

            delete_count = count_width(item, align_zh) - count_width(item, False)
            row_str += f'|{item:^{cw-delete_count+2}}'

        row_str += "|"
        print(row_str)
```
举例如下
**example 1： 上篇中用到的表格**
```python
column = ["`conversion`", "说明" , "示例", "输出"]
rows = [
    ["`s`", "对结果调用`str()`方法" , '`f"His name is {name!s}."`', """`'His name is Ståle.'`"""],
    ["`r`", "对结果调用`repr()`方法" , '`f"His name is {name!r}."`', """`"His name is 'Ståle'."`"""],
    ["`a`", "对结果调用`ascii()`方法" , '`f"His name is {name!a}."`', """`"His name is 'St\\xe5le'."`"""],
]

print_to_markdwon_table(column, rows)
```
其输出内容为
```markdwon
| `conversion` |        说明        |             示例             |             输出              |
|     ----     |       ----       |            ----            |            ----             |
|     `s`      |  对结果调用`str()`方法  | `f"His name is {name!s}."` |   `'His name is Ståle.'`    |
|     `r`      | 对结果调用`repr()`方法  | `f"His name is {name!r}."` |  `"His name is 'Ståle'."`   |
|     `a`      | 对结果调用`ascii()`方法 | `f"His name is {name!a}."` | `"His name is 'St\xe5le'."` |
```

展示效果为：

| `conversion` |        说明        |             示例             |             输出              |
|     ----     |       ----       |            ----            |            ----             |
|     `s`      |  对结果调用`str()`方法  | `f"His name is {name!s}."` |   `'His name is Ståle.'`    |
|     `r`      | 对结果调用`repr()`方法  | `f"His name is {name!r}."` |  `"His name is 'Ståle'."`   |
|     `a`      | 对结果调用`ascii()`方法 | `f"His name is {name!a}."` | `"His name is 'St\xe5le'."` |


**example 2： 数据库内容展示**

```python
column = ["id", "name", "sex", "age"]

rows = [
    [0, 'Li Hua', 'male', 20],
    [1, 'Big Shuang', 'male', 24],
    [2, 'Xiao Hong', 'female', 21],
    [3, 'Xiao Hua', 'female', 19],
    [4, 'Ellen', 'female', 20],
    [5, 'Zhang Sirui', 'female', 22],
    [6, 'Alex', 'male', 23],
    [7, 'Zhao Wen', 'female', 24],
    [8, 'Sun Wu', 'male', 18],
    [9, 'Qian Kong', 'male', 22]
]

print_to_markdwon_table(column, rows)
```
其输出内容为
```markdown
| id |    name     |  sex   | age |
|----|    ----     |  ----  |---- |
| 0  |   Li Hua    |  male  | 20  |
| 1  | Big Shuang  |  male  | 24  |
| 2  |  Xiao Hong  | female | 21  |
| 3  |  Xiao Hua   | female | 19  |
| 4  |    Ellen    | female | 20  |
| 5  | Zhang Sirui | female | 22  |
| 6  |    Alex     |  male  | 23  |
| 7  |  Zhao Wen   | female | 24  |
| 8  |   Sun Wu    |  male  | 18  |
| 9  |  Qian Kong  |  male  | 22  |
```
展示效果为：

| id |    name     |  sex   | age |
|----|    ----     |  ----  |---- |
| 0  |   Li Hua    |  male  | 20  |
| 1  | Big Shuang  |  male  | 24  |
| 2  |  Xiao Hong  | female | 21  |
| 3  |  Xiao Hua   | female | 19  |
| 4  |    Ellen    | female | 20  |
| 5  | Zhang Sirui | female | 22  |
| 6  |    Alex     |  male  | 23  |
| 7  |  Zhao Wen   | female | 24  |
| 8  |   Sun Wu    |  male  | 18  |
| 9  |  Qian Kong  |  male  | 22  |