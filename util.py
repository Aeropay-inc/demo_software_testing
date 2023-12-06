


def int_generator():
    if not hasattr(int_generator, "next_ret"):
        int_generator.next_ret = 1

    ret = int_generator.next_ret
    int_generator.next_ret += 1
    return ret

