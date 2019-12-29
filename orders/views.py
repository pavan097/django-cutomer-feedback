from django.shortcuts import render
from django.http import HttpResponse
from orders.models import ReturnOrder

def returnOrders(request):
    if request.method == 'POST':
        print('post request is called')
        product_id = request.POST['prod_id']
        product_type = request.POST['prod_type']
        email = request.POST['email']
        phone_no = request.POST['phn_no']
        description = request.POST['description']
        print('product id is :',product_id)
        print('product_type is :',product_type)
        print('email id is :',email)
        print('phone_no is :',phone_no)
        print('description is :',description)
        data = ReturnOrder(product_id=product_id, product_type=product_type, user_email=email, phone_no=phone_no, description=description)
        data.save()
        return HttpResponse('Success')
    return render(request,'orders/return_orders.html',{})

def checkRequests(request):
    data = ReturnOrder.objects.all()
    print('all the database data :',data)
    return render(request, 'orders/check_requests.html',{'data':data})