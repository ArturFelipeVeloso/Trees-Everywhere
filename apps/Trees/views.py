from django.shortcuts import render, redirect

# import models
from .models import Plant, PlantedTrees
from apps.Accounts.models import Profile, Account
from django.contrib.auth.models import User

# import timezone
from datetime import datetime

# import forms
from .forms import PlantedTreesForm

# Verify login on template
from django.contrib.auth.decorators import login_required

# AST import
import ast

# Convert str to tuple function
def parse_tuple(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return

# Home View
def home(request):
    if request.user.is_authenticated:
        # My Planted Trees
        my_planted_trees = PlantedTrees.objects.filter(user=request.user)
        
        # My Accounts
        accounts = Account.objects.filter(user__id=request.user.id)
        
        # Blank lists
        all_planted_trees_my_accounts = []
        users = []
        
        # For in my accounts
        for account in accounts:
            user_id_list = list(account.user.all().values_list('id', flat=True))
            
            # If exists user id add to users list
            if user_id_list:
                for user_id in user_id_list:
                    users.append(User.objects.get(id=user_id))
        
        # Remove repeats of user id
        users = dict.fromkeys(users)
        users = list(users)
        
        # For in my users list to get all 
        for user_accounts in users:
            
            # If the user id is diferrent of user logged id, to add in my list of all planted trees
            if user_accounts.id != request.user.id:
                all_planted_trees_my_accounts.append(PlantedTrees.objects.filter(user__id=user_accounts.id))
    
        data = {
            "my_planted_trees": my_planted_trees,
            "all_planted_trees_my_accounts": all_planted_trees_my_accounts,
        }

    else:
        data = {}
        
    return render(request, "home.html", data)

# Planted Trees Forms Add
@login_required
def addPlantedTree(request):
    planted_trees = PlantedTrees.objects.filter(user=request.user)
    
    if request.method=='POST':
        form = PlantedTreesForm(request.POST)
        if form.is_valid():
            #try:
                
            locations = request.POST.get('name_lat_long')
            locations = parse_tuple(locations)
            
            if type(locations[0]) is tuple:
                for location in locations:
                    tree = Plant.objects.get(id=int(request.POST.get('tree')))
                    PlantedTrees.objects.create(
                        user = request.user,
                        age = int(request.POST.get('age')),
                        tree = tree,
                        about = request.POST.get('about'),
                        location_lat = location[0],
                        location_long = location[1],
                        planted_at = datetime.now()
                    )
            elif locations:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.location_lat = locations[0]
                instance.location_long = locations[1]
                instance.planted_at = datetime.now()
                print(instance)
                instance.save()
            else:
                print("Error in location field")
                    
            #except:  
                #print("Error in save") 
        else:
            print("Error in form")
        
        return redirect('home')
    
    else:
        form = PlantedTreesForm()
        
        data = {
            "form": form
        }
        
        return render(request, "form_planted_tree.html", data)
    
    
# Planted Trees Forms Edit
@login_required
def editPlantedTree(request, planted_tree_id):
   
    planted_trees = PlantedTrees.objects.get(id=planted_tree_id)
    if planted_trees.user == request.user:
        if request.method=='POST':
            form = PlantedTreesForm(request.POST, instance = planted_trees)
            if form.is_valid():
                try:  
                    form.save()
                except:  
                    print("Error to save") 
            else:
                print("Error in form")
            
            return redirect('home')
        
        else:
            form = PlantedTreesForm(instance = planted_trees)
            
            data = {
                "form": form
            }
            
            return render(request, "form_edit_planted_tree.html", data)
    else:
        return redirect('home')
    
# Planeted Tree View
@login_required
def viewPlantedTree(request, planted_tree_id):
    planted_trees = PlantedTrees.objects.get(id=planted_tree_id)
        
    data = {
        "platend_trees": planted_trees, 
    }
        
    return render(request, "view_planted_tree.html", data)