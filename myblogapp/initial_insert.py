# Python3!
# 向数据库插入新增文章的信息

import os
from bs4 import BeautifulSoup
from myblog.settings import BASE_DIR
from myblogapp.models import Skill,Life,Food

path = os.path.join(BASE_DIR, 'myblogapp/templates/skill/')

def get_new_article():
    """
    获取新增文章的文件名
    :return: 文件名
    """
    file_list = os.listdir(path)
    if file_list:
        for file_name in file_list:
            yield file_name

def parse_html(file_name):
    """
    或许新增文章的基本信息
    :param file_name: 新增文章名
    :return: 基本信息
    """
    file_path = path + file_name
    with open(file_path,'r',encoding='utf-8',) as file:
        htmlhandle = file.read()
        soup = BeautifulSoup(htmlhandle,'lxml')
        title = soup.select(".article-title")[0].text.strip()
        sort = soup.select(".article-sort")[0].text.strip()
        type = soup.select(".article-sort-type")[0].text.strip()
        time = soup.select(".article-time")[0].text.strip()
        abstract = soup.select(".article-abstract-text")[0].text.strip()
        if sort == "技术杂谈":
            href = "/skill/" + file_name
        if sort == "生活记录":
            href = "/life/" + file_name
        if sort == "美食":
            href = "/food/" + file_name
        return sort,type,title,abstract,href,time

def insert(msg_tuple):
    sort, type, title, abstract, href, time = msg_tuple
    print(sort, type, title, abstract, href, time)
    if sort == "技术杂谈":
        Skill.type = type
        Skill.title = title
        Skill.abstract = abstract
        Skill.href = href
        Skill.time = time
        Skill.save()
    if sort == "生活记录":
        Life.type = type
        Life.title = title
        Life.abstract = abstract
        Life.href = href
        Life.time = time
        Life.save()
    if sort == "美食":
        Food.type = type
        Food.title = title
        Food.abstract = abstract
        Food.href = href
        Food.time = time
        Food.save()

if __name__ == "__main__":
    for file_name in get_new_article():
        msg_tuple = ()
        msg_tuple = parse_html(file_name)
        insert(msg_tuple)
        print("OK")