# Alice 和 Bob 再次设计了一款新的石子游戏。现有一行 n 个石子，每个石子都有一个关联的数字表示它的价值。给你一个整数数组 stones ，其中 stones[i] 是第 i 个石子的价值。

# Alice 和 Bob 轮流进行自己的回合，Alice 先手。每一回合，玩家需要从 stones 中移除任一石子。

# 如果玩家移除石子后，导致 所有已移除石子 的价值 总和 可以被 3 整除，那么该玩家就 输掉游戏 。
# 如果不满足上一条，且移除后没有任何剩余的石子，那么 Bob 将会直接获胜（即便是在 Alice 的回合）。
# 假设两位玩家均采用 最佳 决策。如果 Alice 获胜，返回 true ；如果 Bob 获胜，返回 false 。

# 思路与算法

# 由于玩家的目标是使得已经被移除的石子的价值总和不是 33 的倍数，因此我们可以把石子分成三类，它们的价值除以 33 的余数分别为 0, 1, 20,1,2。我们可以直接用 0, 1, 20,1,2 代表它们的价值，对应的石子数量分别为 \textit{cnt}_0, \textit{cnt}_1, \textit{cnt}_2。

# 可以发现，移除类型 0 的石子并不会对总和产生影响，因此类型 0 的石子可以看成是「先后手」交换。具体地，例如当前是 Alice 在进行操作，它发现如果自己选择移除类型 1 或 2 的石子，那么她在最后一定不能获胜。这时它就可以选择移除一个类型 0 的石子，将同样的局面交给 Bob。如果类型 0 的石子还没有移除完，那么 Bob 同样可以通过移除一个类型 0 的石子将局面重新交给 Alice。这样不断地往复下去，我们可以得到结论：

    # 如果类型 00 的石子的个数为偶数，那么胜负情况等价于没有类型 00 的石子的胜负情况；

    # 如果类型 00 的石子个数为奇数，那么胜负情况等价于只有 11 个类型 00 的石子的胜负情况。注意这里不能单纯地等价于「没有类型 0 的石子的胜负情况」的相反情况，这是因为如果所有的石子都被移除完，无论谁移除了最后一个石子，都算 Alice 输。因此如果 Alice 发现自己选择移除类型 1 或 2 的石子不能获胜，于是选择移除类型 00 的石子，并且它不能获胜的原因是「石子会移除完」，那么 Alice 仍然会输。

# 将类型 0 的石子考虑完全之后，我们就还剩下类型 1 和 2 的石子了。可以发现，为了保证移除石子的和不为 3 的倍数，操作顺序只有可能为下面的两种情况：

    # 如果 Alice 首先移除类型 1 的石子，那么 Bob 只能移除类型 1 的石子，在这之后 Alice 只能移除类型 2 的石子，Bob 同样只能移除类型 1 的石子。以此类推，移除石子的类型序列为：

    # 1121212121⋯

    # 如果 Alice 首先移除类型 22 的石子，我们可以类似得到移除石子的类型序列为：

    # 2212121212⋯

# 作为先手的 Alice 可以在二者中选择一个序列。例如 Alice 选择第一种，那么 Bob 永远移除类型 1 的石子，Alice 除了第一步移除类型 1 的石子之外，后续永远移除类型 2 的石子。因此 Alice 可以获胜当且仅当：

    # 类型 1 的石子恰好有 1 个，并且类型 2 的石子至少有 1 个。此时 Alice 在 Bob 完成第一步时获胜；

    # 类型 1 的石子至少有 2 个，并且不能比类型 2 的石子多：

        # 如果多 1 个，那么在 Alice 移除最后一个类型 22 的石子后，所有的石子都被移除，Bob 获胜；

        # 如果多 2 个，那么在 Bob 移除最后一个类型 11 的石子后，所有的石子都被移除，Bob 获胜；

        # 如果多超过 22 个，那么 Alice 会在某一步没有类型 22 的石子可以移除，Bob 获胜；

        # 如果一样多或类型 22 的石子更多，那么 Bob 会在某一步没有类型 11 的石子可以移除，Alice 获胜。

# 上面的两个条件可以归纳为同一个条件，即有类型 11 的石子，并且不能比类型 22 的石子多。

# 同理，如果 Alice 选择第二种，那么她获胜当且仅当有类型 22 的石子，并且不能比类型 11 的石子多。

# 上述的两种情况也可以归纳为同一种情况，即类型 11 和类型 22 的石子至少都有 11 个。

# 细节

# 回到前面关于类型 00 石子的讨论，可以得到 Alice 获胜的条件：

    # 如果类型 00 的石子的个数为偶数，那么 Alice 获胜当且仅当类型 11 和类型 22 的石子至少都有 11 个；

    # 如果类型 00 的石子的个数为奇数，那么 Alice 获胜当且仅当「在没有类型 00 石子的情况下，Bob 获胜且原因不是因为所有石子都被移除」。对应到上面的分析即为「类型 11 的石子比类型 22 多超过 22 个」或者「类型 22 的石子比类型 11 多超过 22 个」。
