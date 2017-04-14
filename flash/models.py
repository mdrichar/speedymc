from django.db import models

# Create your models here.

class Factoid(models.Model):
    fid = models.IntegerField(default=0)
    factor1 = models.IntegerField(default=0)
    factor2 = models.IntegerField(default=0)

    def __str__(self):
        return str(self.factor1) + "*" + str(self.factor2) + "=" + str(self.factor1*self.factor2)

class BinaryFact(models.Model):
    operand1 = models.IntegerField(default=0)
    operand2 = models.IntegerField(default=0)
    operator = models.CharField(max_length=1)

    def __str__(self):
        return str(self.operand1) + self.operator + str(self.operand2)

class User(models.Model):
    name = models.CharField(max_length=40);

    def __str__(self):
        return str(self.name) 

class QuestionSet(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=512)
    binary_facts = models.ManyToManyField(BinaryFact, related_name='qsets')

    def __str__(self):
        return str(self.name) 

class Bout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    elapsed = models.IntegerField(default=0)
    correct_cnt = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + str(self.user) + str(self.question_set) + ":" + str(self.elapsed)


class ResponseTiming(models.Model):
    bout = models.ForeignKey(Bout, on_delete=models.CASCADE)
    binary_fact = models.ForeignKey(BinaryFact, on_delete=models.CASCADE)
    elapsed = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.bout) + str(self.binary_fact) + ":" + str(self.elapsed)





