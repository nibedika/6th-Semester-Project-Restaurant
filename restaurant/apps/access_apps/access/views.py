# Buildin Package
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from package.helper import Helper as hp
from django.db.models import Q as Q_set
import time

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.order.models import Table as orderDB
from apps.backend_apps.food.models import Table as foodDB


# Create your views here.
class Access():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg


	def sign_up(request):
		if request.method == 'POST' and request.POST.get('sign_up'):

			data = userDB(
				user_id        = hp.unique_custom_id(hp, 'U'),
				name           = request.POST.get('name'),
				username       = request.POST.get('username'),
				email          = request.POST.get('email'),
				password       = request.POST.get('password'),
				confirmed_pass = request.POST.get('confirmed_pass'),
				designation    = request.POST.get('designation'),
			)

			# Username and Email existance check start
			username     = request.POST.get('username')
			email        = request.POST.get('email')
			usernameCond = Q_set(username=username)
			usernameCond = Q_set(email=email)

			usernameExists = False
			emailExists    = False

			if userDB.objects.filter(usernameCond).exists():
				usernameExists = True
			else:
				usernameExists = False

			if userDB.objects.filter(usernameCond).exists():
				emailExists = True
			else:
				emailExists = False

			if usernameExists == False and emailExists == False:
				status = data.save()
				return redirect('sign_in')
			else:
				pass

		elif request.method == 'GET':
			return render(request, 'sign_up.html')
		return render(request, 'sign_up.html')



	def sign_in(request):
		if request.method == 'POST' and request.POST.get('sign_in'):
			loginUsername = request.POST.get('username')
			loginPassword = request.POST.get('password')

			userWhere     = Q_set(username=loginUsername)

			userExixtance = True
			if userDB.objects.filter(userWhere).exists():
				usernameExists = True
			else:
				usernameExists = True

			if userExixtance == True:
				where    = Q_set(username=loginUsername)
				userInfo = get_object_or_404(userDB, where)

				if userInfo:
					if userInfo.username == loginUsername and userInfo.confirmed_pass == loginPassword:
						request.session['username'] = loginUsername
						return redirect('home')
					else:
						return redirect('sign_up')
				else:
					pass
			else:
				return redirect('sign_up')
		elif request.method == 'GET':
			return render(request, 'sign_in.html')



	def home(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			orderWhere      = Q_set(status='active', trash=False)
			orderInfo       = orderDB.objects.filter(orderWhere)
			order           = orderDB.objects.filter(orderWhere).count()
			
			foodWhere       = Q_set(status='active', trash=False)
			foodInfo        = foodDB.objects.filter(foodWhere)
			food            = foodDB.objects.filter(foodWhere).count()

			return render(request, 'home.html', {'menuData': menuInfo, 'orderData': orderInfo, 'order': order, 'food': food})
		else:
			return redirect('sign_out')



	def sign_out(request):
		if request.session.has_key('username'):
			try:
				sessionUsername = request.session['username']
				userWhere       = Q_set(username=sessionUsername)
				menuInfo        = userDB.objects.get(userWhere)

				del request.session['username']
				return redirect('sign_out')
			except:
				return redirect('sign_out')
		else:
			return redirect('sign_up')
		return render(request, 'sign_up.html')



	def view_profile(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			return render(request, 'view_profile.html', {'menuData': menuInfo})
		else:
			return redirect('sign_out')



	def edit_profile(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			# Update Profile Picture And Cover Picture Start Here ------------->
			if request.method == 'POST' and request.POST.get('edit_profile'):

				username = request.session['username']

				if request.FILES.get('profile_picture') != None and request.FILES.get('profile_picture') != '':
					profileImage = hp.file_processor(hp, request.FILES.get('profile_picture'), 'pro_pic', 'profile_img/')
				else:
					profileImage = menuInfo.profile_picture

				# Data entry block start 
				where  = Q_set(username=username)
				pre_update = userDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					name            = request.POST.get('name'),
					password        = request.POST.get('password'),
					confirmed_pass  = request.POST.get('confirmed_pass'),
					designation     = request.POST.get('designation'),
					profile_picture = profileImage
			    )
				# Data entry block end 

				return redirect('view_profile')
			elif request.method == 'GET':
				return render(request, 'edit_profile.html', {'menuData': menuInfo})
			# Update Profile Picture And Cover Picture End Here --------------->

			return render(request, 'edit_profile.html', {'menuData': menuInfo})
		else:
			return redirect('sign_out')



	def delete_profile(request, reUser):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			menuInfo.delete()
			return redirect('sign_out')
		else:
			return redirect('sign_out')
