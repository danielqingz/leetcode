# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split()
        out_str = ''
        i = len(tmp)-1
        while i >= 0:
            out_str += tmp[i]+' '
            i-=1
        return out_str[:-1]

# More clever

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        strs = s.split() # 分割字符串
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])
