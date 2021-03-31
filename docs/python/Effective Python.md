# Effective Python

## Pythonic思考方式

1. 确认自己使用的Python版本
    * 活跃版本：python2、python3，有限考虑python3
    * 运行时环境：CPython、Jython、IronPython以及PyPy等
    * 版本迁移：2to3、six
    * 了解版本差异：range、str等
2. 一致的风格，遵守PEP8: 便于协作、维护
3. 了解bytes、str和unicode差异
4. 辅助函数取代复杂表达式
    * 避免过度运用python特性，写出特别复杂难以理解的单行表达式。反复使用的逻辑，应该移到辅助函数中。
    * 使用if/else比使用or/and boolean表达式更清晰
5. 了解切片的使用：
    * start/end可以越界，不写多余的0或序列长度
    * 序列切片会产生副本
    * 切片赋值不要求长度相等
6. 在单词切片操作内，不要同时指定start、end、stride
    * 可读性差，难以阅读，负数步长难以理解
    * 对于简单的常用的逆序看实际情况，不一概而论
7. 用列表推导取代map或filter
    * 相对map,filter更简洁清晰，无需额外的lambda表达式
    * 跳过序列中元素需要map + filter一起，列表推导可以直接条件过滤
    * 列表推导支持字典和set
8. 不要使用含有2个以上表达的列表推导：难以理解，可读性差
9. 用生成器表达式改写数据量较大的列表推导
    * 列表推导会创建全新列表，数据量很大式会消耗大量内存
    * 生成器表达式返回的迭代器可以放在另一个生成器表达式的for子表达式中，二者结合使用。生成器串联执行速度很快
10. 尽量使用enumerate取代range
    * 可以获取索引和值，避免使用range下标遍历，可以指定起始索引
    * enumerate可以讲各种迭代器包装为生成器
11. 用zip同时遍历2个迭代器
    * 平行组合遍历，python 3相当于生成器遍历逐次产生元组，Python2是一次性返回列表
    * 不等长，会提前终止；不关注长度，可以使用itertools.zip_longest
12. 不要在for/while后使用else
    * 难理解，break退出不调用；某些场景可以简化flag遍历使用，但通常也可用辅助函数完成
13. 合理使用try/except/else/finally每个代码块
    * else: try异常没发生会执行，可以将容易异常的部分放到try中，else中放后续执行代码，减少try中代码量
    * finally资源清理，避免在finally中使用break或return

**总结**：

* 了解python版本
* 了解pythonic特性：bytes、str、slice、列表推导、enumerate、for/else、try/except/else/finally
* 可读性：PEP8规范、辅助函数取代复杂表达式、避免map/filter使用、避免多级列表推导

## 函数

1. 尽量使用异常表示特殊情况，而不是返回None
    * not 空列表、false、0和not None都返回true, 无法准确区分None和其他几种场景
2. 了解闭包中访问外围作用域中变量
    * LEGB
    * nonlocal, python2使用可变对象
3. 考虑使用生成器改写直接返回列表的函数
    * 内存，类似Python中第9条"用生成器表达式改写数据量较大的列表推导", 当前场景在函数中，使用yield
4. 注意默认值得可变参数
