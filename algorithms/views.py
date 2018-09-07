from django.shortcuts import render
from django.http import JsonResponse


from . import algos
from .forms import Eucledian_f

def index(request):
	if request.method == 'POST':
		print(request.POST['num1'],request.POST['num2'])
	return render(request,'algorithms/index.html',{'algorithms':('Eucledian','Extended Eucledian')})

def listView(request):
	return render(request,'algorithms/list.html',{})

def eucledianView(request):
	form = Eucledian_f()
	if request.is_ajax():
		form = Eucledian_f(request.POST)
		if form.is_valid():
			n1 = int(form.data['number1']	)
			n2 = int(form.data['number2']) 
			gcd = algos.eucledian(n1,n2)
			data = {
				'message':'GCD({n1},{n2}) = {gcd}'.format(gcd=gcd,n1=n1,n2=n2),
				'gcd':gcd
			}
			print(gcd)
			return JsonResponse(data)
	context = {
		'form_labels':zip(form,('number1','number2')),
		'form_head':'Eucledian Algorithm',
		'url':'algorithms:eucledian',
	}
	
	return render(request,'algorithms/extended_eucledian.html',context)

def extended_eucledianView(request):
	form = Eucledian_f()
	if request.is_ajax():
		form =Eucledian_f(request.POST)
		if form.is_valid:
			n1 = int(form.data['number1'])
			n2 = int(form.data['number2'])
			gcd,s,t = algos.extended_eucledian(n1,n2)
			data = {
				'message':'GCD({n1},{n2}) = {gcd} = {n1}*({s}) + {n2}*({t})'.format(n1=n1,n2=n2,gcd=gcd,s=s,t=t),
				'gcd':gcd,
				's':s,
				't':t
			}

			return JsonResponse(data)
	context = {
		'form_labels':zip(form,('number1','number2')),
		'form_head':'Extended Eucledian Algorithm',
		'url':'algorithms:extended_eucledian',
	}
	return render(request, 'algorithms/extended_eucledian.html',context)


def m_inverseView(request):
	form = Eucledian_f()
	if request.is_ajax():
		form = Eucledian_f(request.POST)
		if form.is_valid():
			a = int(form.data['number1'])
			m = int(form.data['number2'])
			inv = algos.m_inverse(a,m)
			if inv:
				message = '{a}<sup>-1</sup> mod({m}) = {inv}'.format(a=a,m=m,inv=inv)
			else:
				message = 'does not exist'
			return JsonResponse({'message' : message})

	context = {
		'form_head':'Modular Multiplicative Inverse ',
		'url':'algorithms:m_inverse',
		'form_labels':zip(form,('A','M'))
	}
	return render(request,'algorithms/extended_eucledian.html',context)