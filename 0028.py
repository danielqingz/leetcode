# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        lnd = len(needle)
        lnf = len(haystack)
        if lnd > lnf: return -1

        # 偏移表预处理    
        dic ={v:lnd-k for k,v in enumerate(needle)}
        idx = 0

        while idx+lnd <= lnf:
            # 待匹配字符串
            str_cut = haystack[idx:idx+lnd]
            # 判断是否匹配
            if str_cut == needle:
                return idx
            elif idx+lnd == lnf:
                return -1
            else:
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                nextc = haystack[idx+lnd]
                idx += dic[nextc] if dic.get(nextc) else lnd+1
        return -1


# KMP
# 因为 KMP 利用已匹配部分中相同的「前缀」和「后缀」来加速下一次的匹配。

# 因为 KMP 的原串指针不会进行回溯（没有朴素匹配中回到下一个「发起点」的过程）。
