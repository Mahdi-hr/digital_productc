from django.db import models
class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name='parent',blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField('title' , max_length=50)
    description = models.TextField('description',blank=True)
    avatar = models.ImageField('avatar',blank=True,upload_to='categories/')
    is_enable = models.BooleanField('is_enable',default=True)
    created_time = models.DateTimeField('created_time',auto_now_add=True)
    update_time = models.DateTimeField('update_time',auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
class Product(models.Model):
    title = models.CharField('title' , max_length=50)
    description = models.TextField('description',blank=True)
    avatar = models.ImageField('avatar',blank=True,upload_to='Products/')
    is_enable = models.BooleanField('is_enable',default=True)
    categories = models.ManyToManyField('Category',verbose_name='categories',blank=True)
    created_time = models.DateTimeField('created_time',auto_now_add=True)
    update_time = models.DateTimeField('update_time',auto_now=True)

    class Meta:
        db_table = 'Products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class File(models.Model):
    parent = models.ForeignKey('Product',verbose_name='product',on_delete=models.CASCADE)
    title = models.CharField('title' , max_length=50)
    file = models.FileField('file',upload_to='files/%Y/%m/%d')
    is_enable = models.BooleanField('is_enable',default=True)
    created_time = models.DateTimeField('created_time',auto_now_add=True)
    update_time = models.DateTimeField('update_time',auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'