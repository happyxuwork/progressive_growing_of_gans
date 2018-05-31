from sliced_wasserstein import API

if __name__ == '__main__':
    sw = API(5555, [3,32,32], int, 22);
    sw.say()
    sw.begin('warmup')
    sw.feed('warmup',22)
    sw.end()

