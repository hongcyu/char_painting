# Char Painting

----

![Python](https://badgen.net/badge/Python/3.x/blue) ![Platform](https://badgen.net/badge/Platform/Windows|Linux|macOS/green)

可以访问我的[https://hongcyu.cn/posts/opencv-pictovideo.html](https://hongcyu.cn/posts/opencv-pictovideo.html)查看具体细节

## 整体思路

1. 分离出构成视频的图片
2. 对图片进行ASCII码的转换
3. 将转换好的图片进行合成为视频
4. 通过FFmpeg把原视频音乐添加到输出视频中，并且压制为mp4。

## 注意的事及其使用方法

1. 你可能需要安装opencv和Pillow。如果没有这两个库，通常情况下本脚本会自动帮你安装。如果自动安装失败，请在cmd分别运行`pip3 install opencv-python-headless`、`pip3 install Pillow`。

2. 支持常见的mp4、flv等格式。

3. 需要在main函数中修改你的视频文件路径，默认视频文件名称为input.mp4，放在与本py文件相同的目录里。如果没有找到input.mp4，会自动询问你视频名称。

   最简单的方法：将视频放置在py文件的文件夹下，并修改 video_path后的参数为你的视频名字即可运行。

4. 此外还可以设置多进程处理图片，可自行修改进程数量。

   ```
   if __name__ == '__main__':
      video_path = sys.path[0] + '/input.mp4'  # 把input.mp4改成你的视频名字，注意前面的斜杠要保留
      save_pic_path = sys.path[0] + '/cache_pic'  # 别动
      save_charpic_path = sys.path[0] + '/cache_char'  # 别动
      processes_number = 8  # 使用多少个进程同时处理图片，通常不超过CPU线程数，可以自行设置
   ```

   


5. 为生成的视频添加原视频音轨并且压制为mp4需要预先安装好ffmpeg，如果没有安装ffmpeg，请注释掉或者删掉最后一行
   ```
   write_audio(video_path)
   ```
