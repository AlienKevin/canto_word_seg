import crf

seg = crf.CrfSeg()
sen1 = '今晚的月色真美呀！'
sen2 = '生命在于奋斗！'
sen3 = '小哥哥，别复习了，来玩吧！'

print('测试句:', sen1)
print('分词后:', seg.seg(sen1))

print('测试句:', sen2)
print('分词后:', seg.seg(sen2))

print('测试句:', sen3)
print('分词后:', seg.seg(sen3))