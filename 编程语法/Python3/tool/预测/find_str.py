def find_str(fu_l,zi_l,start=0,chuxian_zuobiao_nl=[]):
    chuxian_zuobiao_l = []
    # chuxian_zuobiao_nl = []
    print("********")
    for i,fu in enumerate(fu_l):
        if i<start:
            # print("跳过{}".format(i))
            continue
        # print(i)
        for j,zi in enumerate(zi_l):
            # print("j",j)
            if fu==zi:
                # 第一次 出现  匹配的第一要是 子串的第一个字符
                if len(chuxian_zuobiao_l) < 1 and fu==zi_l[0]:
                    start = i+1
                    chuxian_zuobiao_l.append(i)
                    # print(chuxian_zuobiao_l)
                    print(fu_l[i],chuxian_zuobiao_l, zi_l, len(chuxian_zuobiao_l) % len(zi_l),"第1次")

                # 第二次 以上出现 判断连续性
                elif len(chuxian_zuobiao_l)>=1:
                    # 假设都找到了就提前退出
                    # if len(chuxian_zuobiao_l) == len(zi_l):
                    #     return chuxian_zuobiao_l

                        # return chuxian_zuobiao_l
                    # 如果这次索引 和 上一次记录的索引 是连续的 那么肯定是差值为1  前后索引肯定是连续的   第三次匹配   你的父元素 肯定等于 zi_l的第三个
                    # print(3,i,chuxian_zuobiao_l[-1])
                    if i - chuxian_zuobiao_l[-1] == 1 and fu==zi_l[len(chuxian_zuobiao_l)]:
                        chuxian_zuobiao_l.append(i)
                        start = i + 1
                        # print(chuxian_zuobiao_l)
                    # 如果出现的位置不连续 那么 第一次的匹配是有问题的
                    # 因为第一次 仅仅是落单的部分匹配而已 我们要找的是连续匹配
                    # 这个时候理论上要退出程序 继续进入这个函数将 start传出去
                    else:
                        # print(start)
                        start = i
                        chuxian_zuobiao_l=[]  # 对对 进入递归的时候 很多条件参数要重置
                        print("jjjj")
                        chuxian_zuobiao_nl=find_str(fu_l, zi_l, start=start,chuxian_zuobiao_nl=chuxian_zuobiao_nl)
                        return chuxian_zuobiao_nl

                    # 应该考虑的更多
                    # 是否数量 已经找齐全了 找齐全了 就要将之前的 索引记录都要清空掉
                    print(fu_l[i],chuxian_zuobiao_l, zi_l, len(chuxian_zuobiao_l) % len(zi_l),"第2+n次")
                    if len(chuxian_zuobiao_l) % len(zi_l) == 0:  # 就是说找到了多次
                        if len(chuxian_zuobiao_l) != 0:  # 追加的时候 至少把第一次排除 也就是 不为空的时候
                            if chuxian_zuobiao_l not in chuxian_zuobiao_nl:
                                chuxian_zuobiao_nl.append(chuxian_zuobiao_l)
                                chuxian_zuobiao_l = []
                                print(chuxian_zuobiao_nl)
                                print("-------------------------->")
                            else:
                                return chuxian_zuobiao_nl

                if len(chuxian_zuobiao_l) < 1 and fu != zi_l[0]:
                    continue


    return chuxian_zuobiao_nl


if __name__ == '__main__':
    fu = "10010010"
    fu_l = [char for char in fu]
    zi = "01"
    zi_l = [char for char in zi]
    print(fu_l)
    print(zi_l)
    chuxian_zuobiao_l = find_str(fu_l, zi_l, start=0,chuxian_zuobiao_nl=[])
    print(chuxian_zuobiao_l)