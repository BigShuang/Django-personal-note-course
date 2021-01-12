## python 格式化输出详解（占位符：%、format、f表达式）——上篇 理论篇

### 0 - 占位符介绍
要实现字符串的拼接，使用占位符是的一种高效、常用的方式。

举个例子，下面是不使用占位符的一种写法，直接使用加号拼接字符串
```python
name = "Li hua"
age = 24
print("Hello "+name+", you are " + str(age) + " years old")
```
换成使用占位符的，可以写为
```python
name = "Li hua"
age = 24
print("Hello %s, you are %d years old" % (name, age))
```

其中`%s`、`%d`便是占位符，顾名思义，其作用就是替后面的变量站住这个位置，
字符串后面的%是一个特殊的操作符，该操作符会将后面的变量值，替换掉前面字符串中的占位符。

对比两种写法，会发现使用占位符可以
- 将字符串中用到变量集中在一起，方便查找和修改
- 避免了反复使用引号，导致的引号对应识别困难
- 能够更直接通顺的看出句子的内容

实际上，占位符的优点还有很多，具体可以在下面的使用中去体会。
目前常用的占位符写法有三种

- %
- format
- f表达式

每种方法下，占位符的写法和意思又有不同。

下面依次介绍下这三种并给出几个使用示例。

### 1 - %
> 参考文献：
> [% (String Formatting Operator)](https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html)
> [printf-style-string-formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)

上文已介绍过，`%`是一个特殊的操作符，该操作符会将后面的变量值，替换掉前面字符串中的占位符。

其详细语法格式如下：
```
"... %[key][flags][width][.precision][length type]conversion type ..." % values
```
其中
```txt
%[key][flags][width][.precision][length type]conversion type
```
是该方法下，占位符详细语法的格式。

依次介绍下上面占位符每个符号每个字段的意思
- `%`: 必须要有的符号。它标记占位符的开始。
- `key`: 选填。映射的键，由带括号的字符序列组成，一般用于后面的values是是字典的场景。
- `flags`: 选填。转换标志(Conversion flags), 会影响某些转换类型的结果。
- `width`: 选填。最小字段宽度。如果指定为“*”（星号），则实际宽度从值中元组的下一个元素读取，要转换的对象位于最小字段宽度和可选精度之后。
- `precision`: 选填。精度，写法为`.precision`（点+精度）。如果指定为“*”（星号），则实际宽度从值中元组的下一个元素读取，要转换的值位于精度之后。
- `length type`: 选填。长度修改器。
- `Conversion type`: 必须要有的符号。转换类型，也标记占位符的开始。

下面依次使用一个小示例展示下上面每个字段的用法
- `Conversion type`

由于这个字段是必选字段，所以最先介绍（`%`写法是固定的，`Conversion type`则必须要选择一个转换类型）
类型有很多，只介绍三个非常常用的，（更多的建议查阅官方文档：[printf-style-string-formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)）

| `Conversion type` |              说明              |
|       ----        |             ----             |
|        `s`        | 字符串（使用`str()`方法转换任何Python对象） |
|        `d`        |            十进制整数             |
|        `f`        |    十进制浮点数(小数), 自动保留六位小数。     |

示例：
```shell
>>> "%s  %s  %s" % ("hello", 3, 3.1415)
'hello  3  3.1415'
>>> "%s  %d  %d" % ("hello", 3, 3.1415)
'hello  3  3'
>>> "%s  %d  %f" % ("hello", 3, 3.1415)
'hello  3  3.141500'
>>> "%s  %f  %f" % ("hello", 3, 3.1415)
'hello  3.000000  3.141500'
```

观察上面的示例，不难看出`s`是一个非常通用的类型，所以很多不讲究的场景，`Conversion type`我通通都用`s`。

- `precision`
对于有小数的场景，设置精度是基本操作。
其写法为`.precision`（点+精度）。
不设置的话，浮点数默认精度值是6。

示例如下
```shell
>>> '%f' % 3.14
'3.140000'
>>> '%.1f' % 3.14
'3.1'
>>> '%.2f' % 3.14
'3.14'
>>> '%.3f' % 3.14
'3.140'
>>> '%.4f' % 3.14
'3.1400'
```

**一般来说，`%`操作符下占位符了解到这里就够了，下面的是比较少用的生僻内容。而且也不实用，复杂的对齐操作推荐使用`format`或`f`表达式。**


- `key` （不常用）

这个选填字段是搭配字典格式的`values`使用的
示例如下
```shell
>>> "%(name)s  %(age)s" % {"name": "Lihua", "age": 20}
'Lihua  20'
>>> "%(name)s  %(age)s" % ({"name": "Lihua", "age": 20})
'Lihua  20'
>>> "%(0)s  %(1)s" % ("Lihua", 20)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: format requires a mapping
```
- `flags` （不常用）

该类型可选择的值有：`#`、`0`、`-`、` `、`+`;
这里只介绍其中几种，（更多的建议查阅官方文档：[printf-style-string-formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)）

| `flags` |                          说明                           |
|  ----   |                         ----                          |
|   `0`   |       数值的转换将被零填充，需搭配`width`使用(示例见下面的`width`中的)。       |
|   `-`   | 转化结果左对齐，需搭配`width`使用(示例见下面的`width`中的)， 该标志符会覆盖`0`标志符。 |
|   ` `   |     空格, 在带符号的转换产生的正数（或空字符串）, 之前留一个空格(方便正负数最后对齐)。      |
|   `+`   |      转换数字后，数字前面将会展示其正负号（“+”或“-”）, 该标志符会覆盖` `标志符。      |

示例如下
```shell
>>> "% d  %+d" % (1234, 1234)
' 1234  +1234'
>>> "% d  %+d" % (-1234, -1234)
'-1234  -1234'
```

- `width`
设置字段的最小占位宽度，默认右对齐，内容不够时使用空格填充。

```shell
>>> "%4d,%6d,%10f" % (12, 1234, 3.14)
'  12,  1234,  3.140000'
>>> "%04d,%06d,%010f" % (12, 1234, 3.14)  # use '0' flag
'0012,001234,003.140000'
>>> "%-4d,%-6d,%-10f" % (12, 1234, 3.14)  # use '-' flag
'12  ,1234  ,3.140000  '
>>> "%0-4d,%0-6d,%0-10f" % (12, 1234, 3.14)  # '-' flag will override '0' flag
'12  ,1234  ,3.140000  '
```

- `length type` (使用方式未知)

### 2 - format
> 参考文献：[https://docs.python.org/3.6/library/string.html#format-string-syntax](https://docs.python.org/3.6/library/string.html#format-string-syntax)
> 注意：该方法，在python2和3中的语法有些细微的差异，这里介绍python3.6版本的（应该python3都差不多），具体区别查阅对应版本的官方文档。

`str.format()`是Python2.6开始的新功能，是字符串格式化方法之一，它允许多个替换、值格式化。
这个方法允许我们通过位置，格式化连接字符串中的元素。
这个方法是一个非常实用且强大的方法。
对于复杂的对齐要求，首选该方法。

其总的语法格式如下
```python
"... {[field_name][!conversion][:format_spec]} ...".format(arguments)
```
#### `arguments`
首先介绍下`arguments`，其有两种情况：
- 位置参数（Positional Arguments）

```shell
>>> "{} {}".format("Li hua", 24)
'Li hua 24'
>>> "{0} {1} {1} {0}".format("Li hua", 24)
'Li hua 24 24 Li hua'
>>> "{} {} {} {}".format("Li hua", 24)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: tuple index out of range
```

- 关键字参数（Keyword Arguments）
```shell
>>> "{name} {age}".format(name="Li hua", age=24)
'Li hua 24'
>>> "{name} {age} {age} {name}".format("Li hua", 24)
'Li hua 24 24 Li hua'
>>> "{} {}".format(name="Li hua", age=24)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: tuple index out of range
```

_补充：其实位置参数和关键字参数可以混用，但是不推荐_

然后介绍下该语法下的占位符格式：
```
{[field_name][!conversion][:format_spec]}
```
- `field_name`: 选填。字段名，常使用其基础格式`arg_name`来指定使用`arguments`哪一个。
对于关键词参数，`arg_name`必须为其中的关键字，（此时该字段是必填项）
比如`"{name} {age}".format(name="Li hua", age=24)`
对于位置参数，`arg_name`必须为序号，（此时该字段可不填，不填则默认第一个为0，从前往后依次+1）
比如`"{0} {1}".format("Li hua", 24)`，`"{} {}".format("Li hua", 24)`
两者效果一样。

拓展：该字段完整语法格式为`arg_name(.attribute_name | [element_index])*`，是在arg_name对应的值为对象、列表或字典时使用，获取其进一步的属性值或者内部值。
这里举一个例子：
```shell
>>> "{0[name]} {0[age]}, {1[0]} {1[1]}".format({"name": "Li hua", "age": 24}, ["Zhang san",24])
'Li hua 24, Zhang san 24'
```
#### `conversion`
选填。变换，**不常用**。
指定时要用`!`来开头，指定后会在格式化之前将`arguments`中对应的值进行类型变换。
其有三个值可以指定，分别为

| `conversion` |          说明          |
|     ----     |         ----         |
|     `s`      |  调用结果对象的`str`方法进行转换  |
|     `r`      | 调用结果对象的`repr`方法进行转换  |
|     `a`      | 调用结果对象的`ascii`方法进行转换 |

#### `format_spec`
选填，格式化具体规范，**核心内容，超常用**。
填写时要用`:`来开头，填写后，会按照其指定的规则来进行格式化。

其详细语法为
```
[[fill]align][sign][#][0][width][grouping_option][.precision][type]
```
其中所有字段均为选填，下面依次介绍下（其中加粗的为常用），
- **`fill`**: 填充内容，如果指定了宽度，但变量长度不够，会使用该字段值进行填充。设置了fill，后面必须显式设置align。
- **`align`**: 对齐方式，有以下值：

| `align` |                                              说明                                               |
|  ----   |                                             ----                                              |
|   `<`   |                                       强制左对齐（绝大多数对象默认使用）                                       |
|   `>`   |                                        强制右对齐（数字类型默认使用）                                        |
|   `=`   | 强制将填充内容放在符号(如果有)之后但数字之前，比如输出成`+000000120`这样的格式。此对齐选项仅对数字类型有效。(当'0'紧接在字段宽度`width`之前时，它将成为默认值。) |
|   `^`   |                                            强制居中对齐                                             |

- `sign`: 符号展现格式，仅对数字类型有效。有以下值：

| `sign` |           说明            |
|  ----  |          ----           |
|  `+`   |  正数负数都展现符号，正数用+，负数用-。   |
|  `-`   |     （默认值），仅负数展现符号。      |
|  ` `   | 负数展现符号，正数前面使用一个空格来占位对齐。 |

- `#`: 复杂生僻，基本不使用，不介绍，有需要的可查阅官方文档（见本部分开头）。

- `0`: 当没有设置对齐方式`align`时, 在宽度字段前面加一个零('0')字符，将等价于填充字符`fill`为`0`且对齐方式`align`为`<`。

- **`width`**: 最小字段宽度，不设置则字段宽度将始终与填充它的数据长度相同（此时对齐方式`align`没有意义）。

- `grouping_option`: 分组选择，有两个选项可选:

| `grouping_option` |       说明        |
|       ----        |      ----       |
|        `,`        | 表示使用逗号作为千位分隔符。  |
|        `_`        | 复杂生僻，基本不使用，不介绍. |

- **`precision`**: 精度,指定时要用`.`来开头,是一个十进制数，指定用'f'和'f'格式化的浮点值在小数点后应该显示多少位,即保留几位小数。

- **`type`**: 类型，决定数据应该如何显示。
有很多值，这里只介绍几个常用的：

| `type` |            说明             |
|  ----  |           ----            |
|  `s`   | 字符串格式。这是字符串的默认类型，可以省略（不填） |
|  `d`   |           十进制整数           |
|  `f`   |   十进制浮点数(小数), 默认保留六位小数    |

补充说明1： fill, align只有设置了width才能生效。

简单示例
```shell
>>> "{:4}{:6},{:10}".format("1", "2", 3.14)  # set width
'1   2     ,      3.14'
>>> "{:4}{:>6}, {:^10}".format("1", "2", 3.14)  # set width, align
'1        2,    3.14   '
>>> "{:_<4}{:0>6}, {:^10}".format("1", "2", 3.14)  # set width, align, fill
'1___000002,    3.14   '
>>> "{:_<4}{:0>6}, {:^10.4f}".format("1", "2", 3.14)  # set width, align, fill, precision, type
'1___000002,   3.1400  '
```

### 3 - f 表达式
> 参考文档：
https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
http://zetcode.com/python/fstring/

这是从Python 3.6开始的一个新功能。
f表达式(f-string), 又名(formatted string literal), 是前缀为“f”或“f”， 用花括号`{}`包裹替换字段的字符串文字。

其简易格式为： `f'{name} is {age} years old'`。
其中花括号`{}`包裹的是替换字段`replacement_field`，相当于上面的占位符，
但是不同于占位符是先占住位置最后标明变量进行替换，f表达式里的替换字段直接在花括号里面进行变量替换。
上面的例子就是用`name`变量值替换`{name}`字段，用`age`变量值替换`{age}`字段。

f表达式详细格式为：
```python
f'(literal_char | {{ | }} | replacement_field)*'
F'(literal_char | {{ | }} | replacement_field)*'
```
以上说明f表达式中的字符串内容，是由任意个`literal_char`、`{{`、`}}`、`replacement_field`自由组成的。

其中literal_char是除花括号`{}`外的任意字符或空。
f表达式中要表示花括号`{}`文本，需要进行转义，转义方式为`{{`, `}}`,


#### `replacement_field`是替换字段，是f表达式的核心。
其格式为
```
{f_expression[=][!conversion][:format_spec]}
```

- 替换字段由花括号包裹
- `f_expression`: 必填内容，常规Python表达式，一般要被圆括号包围，只有少数注意事项：
不允许使用空表达式。
lambda和赋值表达式`:=`必须用显式括号括起来。
替换表达式可以包含换行符（例如在三重引号字符串中），但不能包含注释。
每个表达式在格式化字符串文本出现的上下文中按从左到右的顺序进行计算。

其完整格式为：
```
(conditional_expression | * or_expr) (, conditional_expression | , * or_expr)* [,] | yield_expression
```
过于复杂，只展示不介绍，详情可查阅官方文档：https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-f-expression

- `=`: 选填(3.8新版功能), 在表达式后添加等号'=', 可以显示表达式文本及其求值后的值(在调试中很有用)，。
- `conversion`: 选填。转换，指定时要在开头添加`!`，指定后对表达式求值的结果在格式化之前进行转换。
下方示例中， `name = "Ståle"`

| `conversion` |        说明        |             示例             |             输出              |
|     ----     |       ----       |            ----            |            ----             |
|     `s`      |  对结果调用`str()`方法  | `f"His name is {name!s}."` |   `'His name is Ståle.'`    |
|     `r`      | 对结果调用`repr()`方法  | `f"His name is {name!r}."` |  `"His name is 'Ståle'."`   |
|     `a`      | 对结果调用`ascii()`方法 | `f"His name is {name!a}."` | `"His name is 'St\xe5le'."` |

- `format_spec`: 格式规范， 和本文第二部分`format`中的`format_spec`格式规范是一样的。
不过这里的可以嵌套使用`replacement_field`指定其中的值。


```shell
>>> line = "The output will have the expression text"
>>> f"{line = }"  # use "=" sign, require python 3.8 or above
'line = "The output will have the expression text"'
>>> width = 10
>>> precision = 4
>>> value = 12.34567
>>> f"result: {value:{10}.{4}}"  # set format_spec
'result:      12.35'
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
```


