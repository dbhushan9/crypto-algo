from django.shortcuts import render
from django.http import JsonResponse


from . import algos
from .forms import Eucledian_f

def index(request):
	if request.method == 'POST':
		print(request.POST['num1'],request.POST['num2'])
	return render(request,'algorithms/index.html',{'algorithms':('Eucledian','Extended Eucledian')})

def eucledian(request):
	form = Eucledian_f()

	if request.is_ajax():
		form = Eucledian_f(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			n1 = int(form.data['number1']	)
			n2 = int(form.data['number2']) 
			if(n1 < n2):
				temp =n1 
				n1 = n2
				n2 = temp
			gcd = algos.eucledian(n1,n2)
			data = {
				'message':gcd
			}
			return JsonResponse(data)


	if request.method == 'POST':
		form = Eucledian_f(request.POST)
		if form.is_valid():
			print(form)
			return render(request,'algorithms/eucledian.html',{'form':form,'gcd':gcd,'n1':n1,'n2':n2})
	
	return render(request,'algorithms/eucledian.html',{'form':form})
