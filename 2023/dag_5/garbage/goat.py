class ExitLoop(Exception):
    pass


def find_intersection(range1, range2):
    min_val = min(range1[-1], range2[-1])
    max_val = max(range1[0], range2[0])
    return range(max_val, min_val + 1)


def check(seedrange_lst, mapranges):
    if type(seedrange_lst) != list:
        seedrange_lst = [seedrange_lst]
    unused = seedrange_lst.copy()
    used = []
    try:
        for seedrange in unused:
            for dest_range, src_range in mapranges:
                intersect = find_intersection(seedrange, src_range)
                dest_intersect = range(dest_range[intersect[0] - src_range[0]], 
                        dest_range[intersect[0] - src_range[0] + len(intersect)])
                if intersect:
                    used.append(dest_intersect)
                    if intersect[0] == seedrange[0]:
                        if intersect[-1] == seedrange[-1]:
                            # seed fully contained
                            raise ExitLoop
                        else:
                            # left contained
                            unused.append(range(intersect[-1] + 1, 
                                                seedrange[-1] + 1))
                    elif intersect[-1] == seedrange[-1]:
                        # right fully contained
                        unused.append(range(seedrange[0],
                                            intersect[0]))
                    else:
                        # source fully contained
                        unused.append(range(seedrange[0],
                                            intersect[0]))
                        unused.append(range(intersect[-1] + 1, 
                                            seedrange[-1] + 1))
    except ExitLoop:
        pass