from django.db import models


class Plane(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Message(models.Model):
    title = models.CharField(max_length=120)
    details = models.CharField(max_length=120, null=True)
    value = models.TextField(null=True)
    number = models.IntegerField(null=True)
    plane = models.ForeignKey('Plane', related_name='messages', \
    							 on_delete=models.CASCADE)
        

    def __str__(self):
        return self.title