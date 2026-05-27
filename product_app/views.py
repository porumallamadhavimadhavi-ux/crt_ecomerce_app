from django.shortcuts import render
from django.http import HttpResponse

from . models import ProductModel



# Create your views here.

def add_product(request):
    """
    this function will take the data from client and save into the database
    returns a message with status
    in param it takes the data from the form
    """

    if request.method == 'POST':
        p_name=request.POST.get("p_name")
        p_type=request.POST.get("p_type")
        p_price=request.POST.get("p_price")
        p_quantity=request.POST.get("p_quantity")
        obj=ProductModel.objects.create(
            p_name=p_name,
            p_type=p_type,
            p_price=p_price,
            p_quantity=p_quantity
        )
        return render(request,"success.html",{"message":"product added successfully"})
    return render(request,"product_form.html")

def view_all_product(request):
    """
    this function will return the list of all products
    :param request:no params
    :return:list of products
    """
    data=ProductModel.objects.all().values()
    """ print(list(data))"""



    return render(request,"product_list.html",{"product_data":list(data)})

def delete_by_id(request,id):
    """
    this function will delete a product
    :param request:
    :return:
        """
    if request.method == 'POST':
      data=ProductModel.objects.get(id=id)
      data.delete()
      return render(request,"success.html",{"message":"product deleted successfully"})
    return render(request,"")

