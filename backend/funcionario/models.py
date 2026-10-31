from django.db import models

# Create your models here.


class Funcionario(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Contador(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.funcionario.name} - {self.timestamp}"