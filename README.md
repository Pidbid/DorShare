# DorShare
一个基于Python的局域网文件分享项目  
## 部署方法
- 克隆或下载本仓库到目标主机（树莓派等）  
- 安装Python3 环境以及要用到的库（使用root用户运行）
- > pip install fastapi uvicorn python-multipart 
- 进入DorShare文件夹下运行
- > uvicorn main:app --host '0.0.0.0' --port 80 或 nohup uvicorn main:app --host '0.0.0.0' --port 80 &
- 在其他或本地浏览器输入目标主机的局域网地址
## 文件结构  
DorShare  
-model  
----files.py......编写的文件模块  
-static  
----js  
----css  
----img  
----files......主要的文件存储位置    
--------img......图片文件存储  
--------music......音乐文件存储  
--------video......视频文件存储  
--------oth......其余文件  
-templetes......模板文件夹  
----index.html......模板文件  
-main.py......主要入口文件
## 功能介绍
文件上传，删除，浏览（视频，图片，音乐），文件下载  
![index介绍](https://github.com/Pidbid/DorShare/blob/master/static/files/img/index.png)

## 注
- 后期可能会全部推翻重新改写
- 功能还不完善，需要持续修改
- 作者博客：[歪克士](https://wicos.me/)