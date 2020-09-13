# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.food.models import Table as foodDB
from apps.backend_apps.order.models import Table as orderDB


# Create your views here.
class Order():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg


	def add_order(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			foodWhere       = Q_set(status='active', trash=False)
			foodInfo        = foodDB.objects.filter(foodWhere)

			if request.method == 'POST' and request.POST.get('order_add'):

				orderId = hp.unique_custom_id(hp, 'O')

				# Data entry block start 
				data = orderDB(
					order_id          = orderId,
					bill              = request.POST.get('bill'),
					commission        = request.POST.get('commission'),
					remission         = request.POST.get('remission'),
					customer_name     = request.POST.get('customer_name'),
					customer_contact  = request.POST.get('customer_contact'),
					customer_address  = request.POST.get('customer_address'),
					customer_feedback = request.POST.get('customer_feedback'),
					customer_rating   = request.POST.get('customer_rating'),
				)
				status    = data.save()
				where     = Q_set(order_id=orderId, trash=False)
				addedInfo = orderDB.objects.get(where)

				for food in request.POST.get('food_id'):
					oWhere = Q_set(id=food, status='active', trash=False)
					oInfo  = foodDB.objects.get(oWhere)
					addedInfo.food_id.add(oInfo)

				return redirect('all_order')
			elif request.method == 'GET':
				return render(request, 'order_add.html', {'menuData': menuInfo, 'foodData': foodInfo})

			return render(request, 'order_add.html', {'menuData': menuInfo, 'foodData': foodInfo})
		else:
			return redirect('home')



	def all_order(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			orderWhere       = Q_set(status='active', trash=False)
			orderInfo        = orderDB.objects.filter(orderWhere)

			return render(request, 'order_all.html', {'menuData': menuInfo, 'orderData': orderInfo})
		else:
			return redirect('home')



	def view_order(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			orderWhere       = Q_set(id=id, status='active', trash=False)
			orderInfo        = orderDB.objects.get(orderWhere)

			return render(request, 'order_view.html', {'menuData': menuInfo, 'orderData': orderInfo})
		else:
			return redirect('sign_out')



	def edit_order(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			foodWhere       = Q_set(status='active', trash=False)
			foodInfo        = foodDB.objects.filter(foodWhere)
			
			orderWhere      = Q_set(id=id, status='active', trash=False)
			orderInfo       = orderDB.objects.get(orderWhere)

			# Update Profile Picture And Cover Picture Start Here ------------->
			if request.method == 'POST' and request.POST.get('order_edit'):

				# Data entry block start 
				where       = Q_set(id=id, status='active', trash=False)
				pre_update  = orderDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					bill              = request.POST.get('bill'),
					commission        = request.POST.get('commission'),
					remission         = request.POST.get('remission'),
					customer_name     = request.POST.get('customer_name'),
					customer_contact  = request.POST.get('customer_contact'),
					customer_address  = request.POST.get('customer_address'),
					customer_feedback = request.POST.get('customer_feedback'),
					customer_rating   = request.POST.get('customer_rating'),
					status            = request.POST.get('status'),
			    )
				where     = Q_set(order_id=orderId, trash=False)
				addedInfo = orderDB.objects.get(where)

				for food in request.POST.get('food_id'):

					cond = Q_set(id=food)
					if orderDB.food_id.objects.filter(cond).exists():
						oWhere = Q_set(id=food, status='active', trash=False)
						oInfo  = foodDB.objects.get(oWhere)
						addedInfo.food_id.remove(oInfo)
					else:
						oWhere = Q_set(id=food, status='active', trash=False)
						oInfo  = foodDB.objects.get(oWhere)
						addedInfo.food_id.add(oInfo)

				# Data entry block end
				return redirect('all_order') 
			elif request.method == 'GET':
				return render(request, 'order_edit.html', {'menuData': menuInfo, 'foodData': foodInfo, 'orderData': orderInfo})
			return render(request, 'order_edit.html', {'menuData': menuInfo, 'foodData': foodInfo, 'orderData': orderInfo})
		else:
			return redirect('home')



	def delete_order(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mgp.Q_set(id=id)
				pre_update  = update_data(mgp.mh, studentorder, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vgp.ch.message(vgp.ch, 'danger', msg)
				return redirect('order_all', confirmation=(vgp.vh.value_encrypter(vgp.vh, confirmation)))
			else:
				pass
		else:
			return redirect('reland')



	def delete_order(request, id):
		if request.session.has_key('username'):

			orderWhere       = Q_set(id=id, status='active', trash=False)
			orderInfo        = orderDB.objects.get(orderWhere)

			orderInfo.delete()
			return redirect('all_order')
		else:
			return redirect('home')