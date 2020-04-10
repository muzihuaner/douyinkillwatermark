import requests,re
print("本程序由木子欢儿制作，仅供学习与交流，切勿用于商务用途。开源地址：https://github.com/HuanGeNet/douyinkillwatermark")
share = input("请输入你要去水印的抖音短视频链接：")
pat = '(https://v.douyin.com/.*?/)' 
url = re.compile(pat).findall(share)[0]  #正则匹配分享链接
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36'
}
r = requests.get(url, headers=headers)
pat = 'playAddr: "(.*?)",'
play = re.compile(pat).findall(r.text)[0].replace("playwm", "play")
headers = {
    'user-agent': 'Android',
}
r = requests.get(play, headers=headers, allow_redirects=False)
playurl = r.headers['location']

#自定义文件名保存短视频
name = input("===>正在下载保存视频,请输入视频名称：")
video = requests.get(url=playurl, headers=headers)
with open(name+".mp4", 'wb')as file:
    file.write(video.content)
    file.close()
    print("===>视频下载完成！")

#完事后退出程序
input("===>press enter key to exit!")
