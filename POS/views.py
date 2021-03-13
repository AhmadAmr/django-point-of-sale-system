
from django.shortcuts import render,get_object_or_404,redirect
from . models import  Item ,Category, Order,ItemOrder,Address
from django.views.generic import ListView ,DetailView
from django.utils import timezone
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.template import loader
from render_block import render_block_to_string
from django.template import  Context
from .forms import AddressForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

class listItems(ListView):
    model=Item
    context_object_name = 'item_list'    
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        context = super(listItems, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        try:
            context['order_list']= order=Order.objects.get(user=self.request.user,is_ordered=False)
        except:
            context
        return context

class ItemDetail(DetailView):
    model=Item
    template_name='detail-page.html'


def add_to_cart(request,pk):

    if request.user.is_authenticated :
        
        item = get_object_or_404(Item,pk=pk)
        order_item,created=ItemOrder.objects.get_or_create(item=item,is_ordered=False,user=request.user)
        order_qs=Order.objects.filter(is_ordered=False,user=request.user)
        if order_qs.exists():
            order=order_qs[0]
            if order.items.filter(item__pk=item.pk).exists() :
                print('cooo')
                order_item.quantity +=1
                order_item.save()
            else:
                print('blaaa')
                order.items.add(order_item)
        else:
            print('foo')
            date=timezone.now()
            order=Order.objects.create(order_date=date,user=request.user)
            order.items.add(order_item)
        return HttpResponse('{"status":"success", "msg":"hello"}', content_type='application/json')
    else:
        return HttpResponse('{"status":"fail", "msg":"404"}', content_type='application/json')

def cart_list(request):
    order=Order.objects.get(user=request.user,is_ordered=False)
    context = Context({'order_list': order})
    return_str= render_block_to_string('home-page.html', 'results', context  )
    return HttpResponse(return_str)



class checkout(LoginRequiredMixin,ListView):
    template_name='checkout-page.html'
    
    def get(self, *args, **kwargs):
        try:
            form = AddressForm()
            order=Order.objects.get(user=self.request.user,is_ordered=False)
            address=Address.objects.filter(user=self.request.user,default=True)
            context = { 'form': form,'order_list':order}
            if address.exists():
                context.update({'address':address[0]})
            return render(self.request, "checkout-page.html", context)
        except ObjectDoesNotExist:
            return redirect("/POS")

    def post(self, *args, **kwargs):
        address=Address.objects.filter(user=self.request.user,default=True)
        if address.exists():
            form = AddressForm(self.request.POST ,instance=address[0])
            if form.is_valid():
                form.save()
            return redirect('/POS/checkout')
        else:
            form = AddressForm(self.request.POST or None)
            if form.is_valid():
                phone_no  = form.cleaned_data.get('phone_no')
                print(phone_no)
                area_name = form.cleaned_data.get('area_name')
                street_name = form.cleaned_data.get('street_name')
                apartment_number=form.cleaned_data.get('apartment_number')
                country = form.cleaned_data.get('country')
                default = form.cleaned_data.get('default')
                if is_valid_form([phone_no, area_name, street_name,country,default]):
                    shipping_address = Address(
                        user=self.request.user,
                        phone_no=phone_no,
                        street_name=street_name,
                        area_name=area_name,
                        apartment_number=apartment_number,
                        country=country,
                        default=default,
                        )
                    shipping_address.save()
                #form.save()
                return redirect('/POS/checkout')
        
            else:
             return redirect('/POS')
    