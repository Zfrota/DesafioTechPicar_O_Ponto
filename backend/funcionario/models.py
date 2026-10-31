from django.db import models

# Create your models here.


class Funcionario(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  password = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class Contador(models.Model):
  funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.funcionario.first_name} {self.funcionario.last_name} - {self.timestamp}"


class Meta:
    constraints = [
        models.UniqueConstraint(fields=["poll", "voter_token"], name="one_vote_per_poll")
        ]