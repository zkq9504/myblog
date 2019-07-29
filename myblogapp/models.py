from django.db import models

# 留言板和评论数据表
class MsgComm(models.Model):
    file_name = models.CharField(max_length=50)
    time = models.DateTimeField()
    text = models.CharField(max_length=250)

    class Meta():
        db_table = "msgcomm"

# 所有文章基本信息表
class ArticleMsg(models.Model):
    sort = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    abstract = models.CharField(max_length=250)
    href = models.URLField()
    time = models.DateTimeField()

    class Meta():
        db_table = "articlemsg"
