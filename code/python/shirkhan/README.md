# shirkhan

the python tool for shirkhan
> currently using with project u-open-imla

# Usage

## 安装

```shell
pip install shirkhan
```

## 更新

```shell
 pip install --upgrade shirkhan
```

## 删除

```shell
 pip uninstall  shirkhan
```

```python
from shirkhan import decode, encode, syllabify

encode("xxxx")
decode("yyy")
word = "شىرخان"
print(syllabify(word))

```

# shirkhan 专用脚本库的更多功能示例：

## 分音节

```python
from shirkhan import syllabify

print(syllabify('شىرخان'))

# output ['شىر', 'خان']
```

## 元音辅音组合的向量

```python
from shirkhan import SWord

target_word = "شىرخان"

print(SWord(target_word).tokenize())

# output 010010
```

## 组合向量分组

```python
from shirkhan import SWord, do_group

target_word = "شىرخان"
token = SWord(target_word).tokenize()
retoken = token[::-1]  # 反转
print(do_group(retoken))

# output [['0', '1'], ['0', '0', '1'], ['0']]
```

## 分音原始内容

```python
from shirkhan import SWord, position_transform, embed_delimiter

target_word = "شىرخان"
token = SWord(target_word).tokenize()
retoken = token[::-1]

print(position_transform(target_word, embed_delimiter(retoken)))

# output شىرxخان
```

> 更多使用案例请看 examples目录中的脚本

# 开发，贡献指南

- 本地安装项目，安装时指定可编辑方式安装，这样可以边使用边看效果，甚至调整逻辑时不需要频繁修改源码后重新安装

```shell
pip install --editable shirkhan_lib_path // 这个目录指定到有setup.py为止即可

```