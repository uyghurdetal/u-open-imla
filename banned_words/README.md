# 目录说明

本目录中存放的都是本项目中禁用词的md5值。

## 禁用词声明

- 本目录中禁用词的词源来自网络，都是本人定性为不能在本项目中出现的禁用词。仅代表本人和本项目。
- 这些禁用词没有参考任何组织、机构或者法律相关说明。
- 所有禁用词仅代表在本项目中禁用，严禁任何人以任何形式给予不符实的说明。
- 严禁在任何非法用途中使用
- 严禁以个人名义传播、宣传

> 如果你发现任何不符合法律法规的行为或者问题，请及时和我们联系，或者公开指出问题，我们会以最快的速度处理如果你发现任何不符合法律法规行为或者问题，望你及时和我们联系，或者公开指出问题，我们会最快速度处理

## 注意

文件名上出现 syllablied 的文件内容都是分音节组合得到的，直接匹配单词可能没有太大意义。

`推荐` 使用如下模糊匹配算法来过滤

```python
from shirkhan import similar_word_generator

word = "شىرخاننىڭكى"
print(word)
print(similar_word_generator(word))

# شىرخاننىڭكى
# ['شىرخان', 'شىرخاننىڭ', 'شىر', 'شىرخاننىڭكى']
```

#### 如何过滤禁用词？

Python 代码示例如下：

```python
from shirkhan import md5

benned_word_list = ["x", "y", "z"],
target_word_list = ["a", "b", "c"]
for ww in target_word_list:
    if md5(ww) in benned_word_list:
        print("禁用词")
```