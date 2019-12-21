import cv2 
from PIL import Image,ImageFont,ImageDraw
import os
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
#=========================
#coding:UTF-8
# 视频转字符画含音频version-1
#参考1：https://blog.csdn.net/mp624183768/article/details/81161260
#参考2：https://blog.csdn.net/qq_42820064/article/details/90958577
#参考3：https://blog.csdn.net/zj360202/article/details/79026891
#=========================
def get_char(r,g,b,alpha = 256):
    ascii_char = list("#RMNHQODBWGPZ*@$C&98?32I1>!:-;. ")
    #ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:oa+>!:+. ")
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/len(ascii_char)
    return ascii_char[int(gray/unit)]

#将视频转换为图片 并进行计数，返回总共生成了多少张图片！
def video_to_pic(vp):
    #vp = cv2.VideoCapture(video_path)
    number = 0
    if vp.isOpened():
        r,frame = vp.read()
        if not os.path.exists('cache_pic'):
            os.mkdir('cache_pic')
        os.chdir('cache_pic')
    else:
        r = False
    while r:
        number += 1
        cv2.imwrite(str(number)+'.jpg',frame)
        r,frame = vp.read()
    print('\n由视频一共生成了{}张图片！'.format(number))
    os.chdir("..")
    return number


def img_to_char(image_path,raw_width,raw_height,task):
    width = int(raw_width/ 6)
    height = int(raw_height / 15)
    im = Image.open(image_path).convert('RGB')#必须以RGB模式打开
    im = im.resize((width,height),Image.NEAREST)
    
    txt = ''
    color = []
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j, i))
            color.append((pixel[0],pixel[1],pixel[2])) #将颜色加入进行索引
            if len(pixel)==4 :
                txt +=get_char(pixel[0],pixel[1],pixel[2],pixel[3])
            else:
                txt +=get_char(pixel[0],pixel[1],pixel[2])
        txt += '\n'
        color.append((255,255,255))

    im_txt = Image.new("RGB",(raw_width,raw_height),(255,255,255))
    dr = ImageDraw.Draw(im_txt)
    #font = ImageFont.truetype('consola.ttf', 10, encoding='unic') #改为这个字体会让图片比例改变
    font = ImageFont.load_default().font
    x,y = 0,0
    font_w,font_h=font.getsize(txt[1])
    font_h *= 1.37 #调整字体大小
    for i in range(len(txt)):
        if(txt[i]=='\n'):
            x += font_h
            y = -font_w
        dr.text((y,x),txt[i] ,fill = color[i])
        y+=font_w
    os.chdir('cache_char')
    im_txt.save(str(task)+'.jpg')
    os.chdir("..")
    return 0


def star_to_char(number,save_pic_path):
    if not os.path.exists('cache_char'):
        os.mkdir('cache_char')
    img_path_list = [save_pic_path + r'/{}.jpg'.format(i) for i in range(1,number+1)] #生成目标图片文件的路径列表
    task = 0
    for image_path in img_path_list:
        img_width , img_height = Image.open(image_path).size   #获取图片的分辨率
        task += 1
        img_to_char(image_path, img_width , img_height, task)
        print('{}/{} is finished.'.format(task,number))
    print('=======================')
    print('All image was finished!')
    print('=======================')
    return 0

def jpg_to_video(char_image_path,FPS):
    video_fourcc=VideoWriter_fourcc(*"MP42")  # 设置视频编码器,这里使用使用MP42编码器,可以生成更小的视频文件
    char_img_path_list = [char_image_path + r'/{}.jpg'.format(i) for i in range(1,number+1)] #生成目标字符图片文件的路径列表
    char_img_test = Image.open(char_img_path_list[1]).size   #获取图片的分辨率
    video_writter= VideoWriter('video/new_char_video.avi' , video_fourcc , FPS , char_img_test)
    load = 'loading'
    count = 0 #用来清空load进度条的计数
    for image_path in char_img_path_list:
        img = cv2.imread(image_path)
        video_writter.write(img)
        load = load + '.'
        count += 1
        if count % 50 == 0 :
            load = 'loading'
            print()
        print('\r',load,end='')
    video_writter.release()
    print('\n')
    print('=======================')
    print('The video is finished!')
    print('=======================')

if __name__ == '__main__':
    
    video_path = 'video/miaonei.mp4'
    save_pic_path = 'cache_pic'
    save_charpic_path = 'cache_char'

    vp = cv2.VideoCapture(video_path)
    number = video_to_pic(vp)
    FPS = vp.get(cv2.CAP_PROP_FPS)
    star_to_char(number , save_pic_path)
    vp.release()
    jpg_to_video(save_charpic_path,FPS)
    
