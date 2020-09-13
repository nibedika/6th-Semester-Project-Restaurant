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


# Create your views here.
class Food():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg


	def add_food(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			if request.method == 'POST' and request.POST.get('food_add'):

				# Data entry block start 
				data = foodDB(
					food_id         = hp.unique_custom_id(hp, 'F'),
					name            = request.POST.get('name'),
					regular_price   = request.POST.get('regular_price'),
					current_price   = request.POST.get('current_price'),
					delivery_charge = request.POST.get('delivery_charge'),
					other_charge    = request.POST.get('other_charge'),
					image           = hp.file_processor(hp, request.FILES.get('food_img'), 'food', 'food/')
				)
				status = data.save()
				return redirect('all_food')
			elif request.method == 'GET':
				return render(request, 'food_add.html', {'menuData': menuInfo})

			return render(request, 'food_add.html', {'menuData': menuInfo})
		else:
			return redirect('home')



	def all_food(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			foodWhere       = Q_set(status='active', trash=False)
			foodInfo        = foodDB.objects.filter(foodWhere)

			return render(request, 'food_all.html', {'menuData': menuInfo, 'foodData': foodInfo})
		else:
			return redirect('home')



	def edit_food(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			foodWhere       = Q_set(id=id, status='active', trash=False)
			foodInfo        = foodDB.objects.get(foodWhere)

			# Update Profile Picture And Cover Picture Start Here ------------->
			if request.method == 'POST' and request.POST.get('food_edit'):

				if request.FILES.get('food_img') != None and request.FILES.get('food_img') != '':
					foodFile = hp.file_processor(hp, request.FILES.get('food_img'), 'food', 'food/')
				else:
					foodFile = foodInfo.image

				# Data entry block start 
				where       = Q_set(id=id, status='active', trash=False)
				pre_update  = foodDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					name            = request.POST.get('name'),
					regular_price   = request.POST.get('regular_price'),
					current_price   = request.POST.get('current_price'),
					delivery_charge = request.POST.get('delivery_charge'),
					other_charge    = request.POST.get('other_charge'),
					status          = request.POST.get('status'),
					image           = foodFile
			    )
				# Data entry block end
				return redirect('all_food') 
			elif request.method == 'GET':
				return render(request, 'food_edit.html', {'menuData': menuInfo, 'foodData': foodInfo})
			return render(request, 'food_edit.html', {'menuData': menuInfo, 'foodData': foodInfo})
		else:
			return redirect('home')



	def delete_food(request, id):
		if request.session.has_key('username'):

			if request.method == 'GET':
				where       = mgp.Q_set(id=id)
				pre_update  = update_data(mgp.mh, studentfood, where)
				post_update = pre_update.update(
					trash   = True,
			    )

				msg = {
					'pattern' : 'danger',
					'content' : 'Information Successfully Deleted',
					'style'   : 'danger'
				}

				confirmation = vgp.ch.message(vgp.ch, 'danger', msg)
				return redirect('food_all', confirmation=(vgp.vh.value_encrypter(vgp.vh, confirmation)))
			else:
				pass
		else:
			return redirect('reland')



	def delete_food(request, id):
		if request.session.has_key('username'):

			foodWhere       = Q_set(id=id, status='active', trash=False)
			foodInfo        = foodDB.objects.get(foodWhere)

			foodInfo.delete()
			return redirect('all_food')
		else:
			return redirect('home')