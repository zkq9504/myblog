from django.db import models


# 所有文章基本信息表
class Article(models.Model):
    sort = models.CharField('类别',max_length=10)
    tag = models.CharField('标签',max_length=10)
    name = models.CharField('文章名',max_length=50)
    title = models.CharField('标题',max_length=30)
    abstract = models.CharField('摘要',max_length=250)
    content = models.TextField('内容')
    time = models.DateTimeField('发布时间')

    class Meta():
        db_table = "article"

# 文章评论数据表
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    time = models.DateTimeField('评论时间')
    content = models.CharField('内容',max_length=250)

    class Meta():
        db_table = "comment"
# 留言板表
class Msg(models.Model):
    time = models.DateTimeField('留言时间')
    content = models.CharField('内容',max_length=250)

    class Meta():
        db_table = "msg"
