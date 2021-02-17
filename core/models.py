from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    miniature = models.FileField()
    expiry_date = models.CharField(max_length=120)

    def __str__(self):
        return 'Service name:'.format(self.name)


class ServiceStep(models.Model):
    service_id = models.ForeignKey(Service, related_name='steps', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()

    def __str__(self):
        return 'Service name:' + str(self.title)


class Project(models.Model):
    name = models.CharField(max_length=120)
    text = models.CharField(max_length=120)
    miniature = models.FileField()
    link = models.TextField(blank=True, null=True)
    service_id = models.ForeignKey(Service, related_name='projects', on_delete=models.CASCADE)
    task = models.TextField()
    about_company = models.TextField()

    def __str__(self):
        return 'Project name:' + str(self.name)


class Gallery(models.Model):
    project_id = models.ForeignKey(Project, related_name='gallery', null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    image = models.FileField()

    class Meta:
        unique_together = ['project_id']

    def __str__(self):
        return 'Gallery src:'.format(self.image)
