from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# View for index page
def page(request):
	# return HttpResponse("Hello Rid")
	return render(request, '/en/public/index.html')