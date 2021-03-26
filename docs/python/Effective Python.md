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
    * 切片会产生副本
    * 切片赋值不要求长度相等