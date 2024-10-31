def find_str(fu_l, zi_l, start=0, chuxian_zuobiao_nl=[]):
    chuxian_zuobiao_l = []

    for i, fu in enumerate(fu_l):
        if i < start:
            continue
        for j, zi in enumerate(zi_l):
            if fu == zi:
                if len(chuxian_zuobiao_l) < 1 or i - chuxian_zuobiao_l[-1] == 1:
                    chuxian_zuobiao_l.append(i)
                    if len(chuxian_zuobiao_l) == len(zi_l):
                        chuxian_zuobiao_nl.append(chuxian_zuobiao_l)
                        chuxian_zuobiao_l = []
                        start = i + 1  # 更新下一次搜索的起始位置
                        break  # 跳出内层循环，继续外层循环
                else:
                    # 如果不连续，则递归调用，并将结果返回
                    return find_str(fu_l, zi_l, start=start, chuxian_zuobiao_nl=chuxian_zuobiao_nl)
        if len(chuxian_zuobiao_l) > 0:
            # 如果找到了部分匹配，但不是完整的匹配，则更新起始位置
            start = chuxian_zuobiao_l[-1] + 1
            chuxian_zuobiao_l = []

    # 如果遍历完整个fu_l，则返回最终的chuxian_zuobiao_nl
    return chuxian_zuobiao_nl


if __name__ == '__main__':
    fu = "Rust 开发团队1的1xx意见又非常 重视社区的意见,又非常重视china,又非常重视666"
    fu_l = [char for char in fu]
    zi = "又非常重视"
    zi_l = [char for char in zi]
    print(fu_l, zi_l)
    chuxian_zuobiao_l = find_str(fu_l, zi_l, start=0)
    print(chuxian_zuobiao_l)
