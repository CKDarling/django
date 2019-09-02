####### CREATING A DJANGO SITE #######
 # START DJANGO ENVIRONMENT
 # source activate djangoEnv (OR WHATEVER NAME THE ENVIRONMENT IS)
 # 1. django-admin startproject projName
 # 2. cd projName
 # 3. python manage.py startapp app_name

 ##### CREATE A VIEW #####
 # # Create your views in views.py (An example function shown here)
 # def index(request):
    #my_dict ={"insert":"Hello suck y proj_app dick"}
    #return render (request,"proj_app/index.html",context=my_dict)

###### MAP URLS ######

# create urls.py inside your app
# from django.conf.urls import path
# from proj_app import views
# urlpatterns = [path('',views.index,name='index'),]

# go to urls.py in the project folder and make sure your shit looks like this:
# from django.urls import path,include
# urlpatterns = [
#    path('',views.index,name='index'),
#    path('admin/', admin.site.urls),
#    path('proj_app/',include(proj_app.urls))
#              ]
###### SETUP TEMPLATES #####
# create templates folder inside overall project
# create a folder inside templates that shares application name
# create index.html inside new application name folder
# EDIT YOUR HTML FILE TO BE WHAT YOU WISH

##### ALTERING SETTINGS.PY OF OVERALL PROJECT #####
# add - TEMPLATE_DIR = os.path.join(BASE_DIR,"templates") - under BASE_DIR
# scroll down to DIRS = []
# add - TEMPLATES_DIR, inside the list

# TEST THE CREATION
# python3 manage.py runserver

##### MIGRATE DATABASES #####
# python3 manage.py MIGRATE
# python3 manage.py makemigrations app_name
# python3 manage.py migrate
