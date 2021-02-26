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

# 功能示例：

## 分音节

    思路：
    1. 把单词向量化，按照元音，辅音 的0，1 值生成token 0100100
    2. 从后往前分析 所以需要反转 retoken 0010010
    3. 把retoken 以元音为分界分组 001 001 0
    4. 按照分音节通用算法进行给retoken 植入分隔符
        - 两个元音之间有1个辅音它属于前面的音节
        - 两个元音之间有2个辅音它一个属于前面的，一个属于后面的
        - 两个元音之间有3个辅音 第一个属于前面的，后两个属于后面的
        - 两个元音之间有4个辅音 第一个属于前面的，其后的两个一组，最后一个属于后面的   【shirkhan 给自己出的规则，目前没有任何凭据这么做，而且是不对的】
        - 两个元音之间有5个辅音 第一个属于前面的，其后的三个一组，最后一个属于后面的   【shirkhan 给自己出的规则，目前没有任何凭据这么做，而且是不对的】

    5. 把嵌入分割符的retoken分割点坐标映射到原始内容上 i -> len(word)-i
    6. 按照分割符切割

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
from shirkhan import SWord

target_word = "شىرخاننىڭمۇ"
sw = SWord(target_word)
gtoken = sw.get_grouped_token()
gretoken = sw.get_grouped_retoken()

print(sw.tokenize())
print(gtoken)
print(gretoken)

# 01001001001
# [['0', '1'], ['0', '0', '1'], ['0', '0', '1'], ['0', '0', '1']]
# [['1'], ['0', '0', '1'], ['0', '0', '1'], ['0', '0', '1'], ['0']]
```

## 分音原始内容

```python
from shirkhan import SWord

target_word = "شىرخاننىڭمۇ"
sw = SWord(target_word)
print(sw.get_positional_word())
print(sw.get_positional_token())
print(sw.get_positional_retoken())

# شىرxخانxنىڭxمۇ
# 010x010x010x01
# 10x010x010x010
```

## 单词生成字单词

```python
# 第一种方式
from shirkhan import SWord

target_word = "شىرخاننىڭمۇ"
sw = SWord(target_word)
print(sw.get_similar_words())

# 第二种方式
from shirkhan import SWord,similar_words

target_word = "شىرخاننىڭمۇ"
print(similar_words(target_word))


# output:
# ['شىر', 'شىرخان', 'شىرخاننىڭ', 'شىرخاننىڭمۇ']

```

# 开发，贡献指南

- 本地安装项目，安装时指定可编辑方式安装，这样可以边使用边看效果，甚至调整逻辑时不需要频繁修改源码后重新安装

```shell
pip install --editable shirkhan_lib_path // 这个目录指定到有setup.py为止即可

```