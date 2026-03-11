def test1(*args):
    print(args)


test1('amao', 'conia')


def test2(**kwargs):
    print(kwargs)


test2(name='zhangsan', gender='boy', age=18)
