import django
django.setup()
from flash.models import BinaryFact
#bf = BinaryFact(operand1=9,operand2=10,operator='*')
#bf.save()
#BinaryFact.objects.all().delete()
for i in range(2,20):
	for j in range(i,21):
		bf = BinaryFact(operand1=i,operand2=j,operator='*')
		bf.save()
