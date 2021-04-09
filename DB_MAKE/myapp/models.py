from django.db import models


# Create your models here.

class DB_links(models.Model):
    """链接表"""
    link_name = models.CharField(max_length=50, null=True, blank=True)      # 链接名称
    link_url = models.CharField(max_length=100, null=True, blank=True)      # 链接地址

    def __str__(self):
        return self.link_name
