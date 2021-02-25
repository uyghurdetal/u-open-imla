# python folder

这个目录中存放 u-open-imla 处理数据使用的到的辅助脚本的 Python 代码

# shirkhan 专用脚本库功能：

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
