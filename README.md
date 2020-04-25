可以访问我的[blog](https://hongcyu.cn/posts/43462.html)查看具体细节

## 整体思路

1. 分离出构成视频的图片
2. 对图片进行ASCII码的转换
3. 将转换好的图片进行合成为视频
4. 本次为了方便测试，未添加删除生成文件的代码，需要手动删除或者自己添加代码。

## 注意的事及其使用方法

1. 你需要安装opencv，在cmd中输入：**pip3 install opencv-python**

2. 还需要安装pillow，在cmd中输入：**pip3 install pillow**

3. 需要在main函数中修改你的视频文件路径

   将视频放置在py文件的文件夹下，并修改 video_path后的参数为你的视频路径名字即可运行

   ```
   if __name__ == '__main__':
       
       video_path = 'video/heiren.mp4'
       save_pic_path = 'cache_pic'
       save_charpic_path = 'cache_char'
   ```

   

4. 生成的文件不会自己删除需要手动删除
