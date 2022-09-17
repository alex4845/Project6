from django.db import models

class List1(models.Model):
    name1 = models.CharField(max_length=35)

    def __str__(self):
        return self.name1

class List2(models.Model):
    name2 = models.CharField(max_length=40)
    list1 = models.ForeignKey(List1, on_delete=models.PROTECT)

    def __str__(self):
        return self.name2

class List3(models.Model):
    img1 = models.ImageField(upload_to="shtors/", blank=True, null=True)
    img2 = models.ImageField(upload_to="shtors/", blank=True, null=True)
    img3 = models.ImageField(upload_to="shtors/", blank=True, null=True)
    list2 = models.ForeignKey(List2, on_delete=models.PROTECT)

class User_list(models.Model):
    name = models.CharField(max_length=25, null=False)
    date_go = models.CharField(max_length=25)

    def __str__(self):
        return self.date_go

class User_question(models.Model):
    name = models.CharField(max_length=25, null=False)
    question = models.TextField(max_length=300)

    def __str__(self):
        return self.name