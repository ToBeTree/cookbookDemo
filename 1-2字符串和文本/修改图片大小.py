# 跨行去匹配
#-*- conding: utf-8 -*-

# from PIL import Image

# im = Image.open(r'D:\\Learn\PythonProject\2.jpg')
# # im = IMage.open(r'C:\\Users\\wuyongqiang\\Desktop\\泡泡表情包\\金馆长版本贴吧泡泡表情')
# print(im.format, im.size, im.mode)

# # 里面的tuple参数 表示的是？ 900x1600 -->56x100
# img = im.resize((358, 441))
# # help(img)
# img.save('2_can.jpg')


from PIL import Image
import os
# print(os.listdir('E:\\金馆长版本贴吧泡泡表情'))
i = 0
for im_name in os.listdir('C:\\Users\\wuyongqiang\\Desktop\\泡泡表情包\\扁平化贴吧泡泡表情'):
# C:\Users\wuyongqiang\Desktop\泡泡表情包\扁平化贴吧泡泡表情
    im = Image.open('C:\\Users\\wuyongqiang\\Desktop\\泡泡表情包\\扁平化贴吧泡泡表情\\' + im_name)
    print(im.format, im.size, im.mode)
    # 'a'.join(str(im.format))
    # print(im_name.split('.')[0] + '.' + (str(im.format)))
    img = im.resize((64, 64))
    # r'E:\\金馆长版本贴吧泡泡表情\\重制版\\'
    img.save(im_name.split('.')[0]+'.'+(str(im.format)))
    # if im_name.endswith('.jpg'):
    #     img.save(str(i) + '.png')
    #     i += 1
    # else:
    #     img.save('c_' + im_name)
