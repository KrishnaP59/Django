from django.db import models

class device(models.Model):

    type = models.CharField(max_length = 100, blank = False)
    price = models.IntegerField()
    choice = (
        ("Approved", "QA Approved"),
        ("Denied", "QA Denied")
    )

    status = models.CharField(max_length = 100,choices = choice, default = "Sold")
    launch = models.DateField()


    class Meta:
        abstract = True

    def __str__(self):
        return "Type : {0} Price : {1}".format(self.type,self.price)

class smartphone(device):
    pass

class laptop(device):
    pass
