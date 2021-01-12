def transform_to_list(lines):

    lst = []
    for line in lines.split("\n"):
        line = line.strip()
        if line:
            for spe in [":", "："]:
                if spe in line:
                    key, value = line.split(spe)

                    key = key.strip()
                    value = value.strip()

                    lst.append([key, value])
                    break

    return lst


lines = """
`<`: 强制左对齐（绝大多数对象默认使用）
`>`: 强制右对齐（数字类型默认使用）
`=`: 强制将填充内容放在符号(如果有)之后但数字之前，比如输出成`+000000120`这样的格式。此对齐选项仅对数字类型有效。(当'0'紧接在字段宽度`width`之前时，它将成为默认值。)
`^`: 强制居中对齐
"""

rows = transform_to_list(lines)