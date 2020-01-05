import random
dateTime = ['1月15日', '2月5日', '2月12日', '2月19日', '2月26日', '3月4日']
speakerAI = [ '李献阳', '于海龙', '田学朋']
speakerBC = ['韩振州', '李江利', '吴献勇',]
random.shuffle(speakerAI)
random.shuffle(speakerBC)
for i in range(0,3):
    print(dateTime[i*2], ':', speakerAI[i])
    print(dateTime[i*2+1], ':', speakerBC[i])
