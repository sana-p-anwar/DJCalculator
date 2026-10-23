from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):

    def post(self, request):
        request_body = request.body
        form_data=loads(request_body)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        result=n1+n2

        print(request_body)


        data = {
            "Sum": result
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class SubtractionView(View):
    
    def post(self, request):
        data = request.body
        form_data=loads(data)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        difference=n1-n2

        print(data)


        data = {
            "Difference": difference
        }

        return JsonResponse(data)


    
@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    
    def post(self, request):
        data = request.body
        form_data=loads(data)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        multiply=n1*n2

        print(multiply)


        data = {
            "Multiplication": multiply
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):

    def post(self, request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 / n2

        print(data)

        data = {
            "Division": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class ExponentView(View):

    def post(self, request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 ** n2

        print(data)

        data = {
            "Exponent": result
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):

    def post(self, request):
        data = request.body
        form_data = loads(data)

        obtained_marks = form_data.get('obtained_marks')
        total_marks = form_data.get('total_marks')

        percentage = (obtained_marks / total_marks) * 100

        print(data)

        data = {
            "Percentage": percentage
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class BMIView(View):

    def post(self, request):
        data = request.body
        form_data = loads(data)

        weight = form_data.get('weight')
        height = form_data.get('height')

        height = height / 100
        bmi = weight / (height ** 2)

        print(data)

        data = {
            "BMI": bmi
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class RectangleView(View):

    def post(self, request):
        data = request.body
        form_data = loads(data)

        length = form_data.get('length')
        breadth = form_data.get('breadth')

        area = length * breadth

        print(data)

        data = {
            "Area": area
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class AgeCalculatorView(View):

    def post(self, request):
        data = request.body
        form_data = loads(data)

        birth_year = form_data.get('birth_year')
        current_year = form_data.get('current_year')

        age = current_year - birth_year

        print(data)

        data = {
            "Age": age
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class SimpleInterestView(View):

    def post(self, request):
        data = request.body
        form_data = loads(data)

        principal = form_data.get('principal')
        rate = form_data.get('rate')
        time = form_data.get('time')

        interest = (principal * rate * time) / 100

        print(data)

        data = {
            "Principal": principal,
            "Rate": rate,
            "Time": time,
            "Simple Interest": interest
        }

        return JsonResponse(data)