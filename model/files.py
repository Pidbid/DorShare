# -*- coding:utf-8 -*-
import os
import platform
import requests as rq
import time

def str2name(strs:str):
    houzhui = strs.split(".")[-1]
    name = str(int(time.time())) + "." + houzhui
    return name

def system():
    if platform.system() == "Windows":
        return 1
    else:
        return 0

def save_log(strs:str):
    pass

def get_file(types: str):
    if system() == 1:
        dirs = os.getcwd().replace("\\", "/") + "/static/files/"+types+"/"
    else:
        dirs = os.getcwd() + "/static/files/"+types+"/"
    video_dir = os.listdir(dirs)
    rt = []
    for i in video_dir:
        rt.append({"name": i, "path": "static/files/"+types+"/"+i})
    return rt

def get_all_file():
    if system() == 1:
        dirs = os.getcwd().replace("\\", "/") + "/static/files/"
    else:
        dirs = os.getcwd() + "/static/files/"
    all_files = os.walk(dirs)
    get_files = []
    for a in all_files:
        j=[]
        for b in a:
            j.append(b)
        get_files.append(j)
    all_type = []
    files=[]
    for i in get_files:
        if get_files.index(i) == 0:
            for dirr in i[1]:
                all_type.append(dirr)
        else:
            for file in i[2]:
                if len(file)==0:
                    continue
                else:
                    files.append({"name":file,"tag":all_type[get_files.index(i)-1]})
    #print(all_type)
    return files

    

def save_file(filename: str, filedata):
    all_type = {"video": ["mp4", "avi"], "music": [
        "mp3", "ogg", "wav"], "img": ["jpg", "bmp", "jpeg", "gif", "png"]}
    types = "oth"
    for i in all_type:
            if filename.split(".")[-1] in all_type[i]:
                types = i
    #print(types)
    if system() == 1:
        dirs = os.getcwd().replace("\\", "/") + "/static/files/"+types+"/"
    else:
        dirs = os.getcwd() + "/static/files/"+types+"/"
    with open(dirs + filename, "wb") as fp:
        for i in range(int(len(filedata)/(1024*1024))+1):
            fp.write(filedata[i*1024*1024:(i+1)*1024*1024])
    if os.path.exists(dirs+filename):
        return {"name":filename,"path": "static/files/"+types+"/"+filename}

def del_file(name:str,types:str):
    if system() == 1:
        dirs = os.getcwd().replace("\\", "/") + "/static/files/"+types+"/"
    else:
        dirs = os.getcwd() + "/static/files/"+types+"/"
    os.remove(dirs+name)
    return {"status":"success"}


def download_file(url:str):
    #判断是否符合http/https/ftp的代码在前端
    gets = rq.get(url)
    types = gets.headers["Content-Type"]
    if "video" in types:
        types = "video"
    elif "image" in types:
        types = "img"
    elif "audio" in types:
        types = "music"
    else:
        types = "oth"
    if system() == 1:
        dirs = os.getcwd().replace("\\", "/") + "/static/files/"+types+"/"
    else:
        dirs = os.getcwd() + "/static/files/"+types+"/"
    with open(dirs+url.split("/")[-1],"wb") as f:
        f.write(gets.content)
    f.close()
    return {"filepath":"static/files/"+types+"/"+url.split("/")[-1]}
# get_video()