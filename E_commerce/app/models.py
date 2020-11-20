from django.db import models
from django.contrib.auth.models import User

class NewUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=80)
    cat_img = models.ImageField(upload_to='categories',null=True,blank=True)

    def __str__(self):
        return self.cat_name

class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    prod_title = models.CharField(max_length=260)
    prod_img = models.ImageField(upload_to='products',null=True,blank=True)
    prod_original_price = models.CharField(max_length=20)
    prod_discounted_price = models.CharField(max_length=20)
    prod_desc = models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.prod_title
