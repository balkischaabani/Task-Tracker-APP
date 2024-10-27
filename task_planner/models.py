from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    descriptionT = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table='task'



class Utilisateur(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
     
    class Meta:
        db_table='utilisateur'

class Deadline(models.Model):
    date = models.DateField()
    class Meta:
        db_table='deadline'


class Project(models.Model):
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    descriptionP = models.TextField(blank=True)
    deadline = models.OneToOneField(Deadline,on_delete=models.CASCADE)
    class Meta:
        db_table='project'


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'


