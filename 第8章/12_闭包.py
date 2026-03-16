def beauty(char, n):
    def show_msg(msg):
        print(char * n + msg + char * n)
    return show_msg

show1 = beauty('#',6)
show1('你好呀')
show1('Conia')


