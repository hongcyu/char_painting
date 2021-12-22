可以访问我的[https://hongcyu.cn/posts/opencv-pictovideo.html](https://hongcyu.cn/posts/opencv-pictovideo.html)查看具体细节

## 整体思路

1. 分离出构成视频的图片
2. 对图片进行ASCII码的转换
3. 将转换好的图片进行合成为视频
4. 本次为了方便测试，未添加删除生成文件的代码，需要手动删除或者自己添加代码。

## 注意的事及其使用方法

1. 你需要安装opencv，在cmd中输入：**pip3 install opencv-python**

2. 需要在main函数中修改你的视频文件路径

   将视频放置在py文件的文件夹下，并修改 video_path后的参数为你的视频名字即可运行
   此外还可以设置多进程处理图片，可自行修改进程数量

   ```
   if __name__ == '__main__':
      video_path = sys.path[0] + '/test.flv'
      save_pic_path = sys.path[0] + '/cache_pic'  # 别动
      save_charpic_path = sys.path[0] + '/cache_char'  # 别动
      processes_number = 8  # 使用多少个进程同时处理图片，通常不超过CPU线程数，可以自行设置
   ```

   

3. 生成的文件不会自己删除需要手动删除

4. 为生成的视频添加原视频音轨并且压制为mp4需要预先安装好ffmpeg，如果没有安装ffmpeg，请注释掉或者删掉最后一行
   ```
   write_audio(video_path)
   ```
