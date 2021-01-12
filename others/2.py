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


# example 1
column = ["`conversion`", "说明" , "示例", "输出"]

rows = [
    ["`s`", "对结果调用`str()`方法" , '`f"His name is {name!s}."`', """`'His name is Ståle.'`"""],
    ["`r`", "对结果调用`repr()`方法" , '`f"His name is {name!r}."`', """`"His name is 'Ståle'."`"""],
    ["`a`", "对结果调用`ascii()`方法" , '`f"His name is {name!a}."`', """`"His name is 'St\\xe5le'."`"""],
]





# example 2
column = ["`type`", "说明"]
rows = [
["`s`", "字符串格式。这是字符串的默认类型，可以省略（不填）"],
["`d`", "十进制整数"],
["`f`", "十进制浮点数(小数), 默认保留六位小数"],
        ]

column = ["id", "name", "sex", "age"]
info_list = [
        ["Li Hua", "male", 20],
        ["Big Shuang", "male", 24],
        ["Xiao Hong", "female", 21],
        ["Xiao Hua", "female", 19],
        ["Ellen", "female", 20],
        ["Zhang Sirui", "female", 22],
        ["Alex", "male", 23],
        ["Zhao Wen", "female", 24],
        ["Sun Wu", "male", 18],
        ["Qian Kong", "male", 22],
    ]

info_list = [[index] + row for index, row in enumerate(info_list)]
print(info_list)
print_to_markdwon_table(column, info_list)


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

# example 3

# column = ["`align`", "说明"]
# # rows = transform_to_list()
# from others.util202 import rows
#
# # print_to_markdwon_table(column, rows)