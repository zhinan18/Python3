# import urllib.request
# import socket
# import re
# import sys
# import os
# targetDir = r"D:\PythonWorkPlace\load"  #文件保存路径
# def destFile(path):
#     if not os.path.isdir(targetDir):
#         os.mkdir(targetDir)
#     pos = path.rindex('/')
#     t = os.path.join(targetDir, path[pos+1:])
#     return t
# if __name__ == "__main__":  #程序执行入口
#     weburl = "http://www.douban.com/"
#     webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#     req = urllib.request.Request(url=weburl, headers=webheaders)  #构造请求报头
#     webpage = urllib.request.urlopen(req)  #发送请求报头
#     contentBytes = webpage.read()
#     for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(contentBytes))):  #正則表達式查找全部的图片
#         print(link)
#         try:
#             urllib.request.urlretrieve(link, destFile(link)) #下载图片
#         except:
#             print('失败') #异常抛出
import re
import urllib.request

# ------ 获取网页源代码的方法 ---
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

# ------ getHtml()内输入任意帖子的URL ------
html = getHtml("https://hot.cnbeta.com/articles/movie/852665.htm")
#html = getHtml("https://hot.cnbeta.com/articles/movie/852167.htm")
# ------ 修改html对象内的字符编码为UTF-8 ------
html = html.decode('UTF-8')

# ------ 获取帖子内所有图片地址的方法 ------
def getImg(html):
    # ------ 利用正则表达式匹配网页内容找到图片地址 ------
    reg = r'src="([.*\S]*\.jpg)"'
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist

imgList = getImg(html)
imgName = 0
for imgPath in imgList:
    # ------ 这里最好使用异常处理及多线程编程方式 ------
    try:
        f = open('D:\\Temp\\'+ str(imgName)+".jpg", 'wb')
        f.write((urllib.request.urlopen(imgPath)).read())
        print(imgPath)
        f.close()
    except Exception as e:
        print(imgPath+" error")
    imgName += 1

print("All Done!")
