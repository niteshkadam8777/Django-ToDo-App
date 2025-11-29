from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import TaskModel
from django.db.models import Q

# Create your views here.

@login_required(login_url='login_')
def home(request):

    if 'q' in request.GET:
        q=request.GET['q']
        print(q)
        all_data=TaskModel.objects.filter( Q(title__icontains=q) & Q(is_delete=False) | Q(desc__icontains=q) & Q(is_delete=False))
    else:
        all_data=TaskModel.objects.filter(is_delete=False)

    return render(request,'home.html',{'data':all_data})
    
@login_required(login_url='login_')
def add(request):

    if request.method == 'POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']
        TaskModel.objects.create(
            title=title_data,
            desc=desc_data
        )
        return redirect('home')
        
    return render(request,'add.html')


@login_required(login_url='login_')
def trash(request):
    all_data=TaskModel.objects.filter(is_delete=True)

    return render(request,'trash.html',{'data':all_data})


@login_required(login_url='login_')
def complete(request):
    return render(request,'complete.html')


@login_required(login_url='login_')
def delete_(request,pk):
    task=TaskModel.objects.get(id=pk)
    task.is_delete=True
    task.save()
    return redirect('home')


@login_required(login_url='login_')
def update(request, pk):
    try:
        task = TaskModel.objects.get(id=pk) 
    except TaskModel.DoesNotExist:
       
        return redirect('home') 

    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        
        task.title = title_data
        task.desc = desc_data
        
        task.save()
        
        return redirect('home')
    
    return render(request, 'update.html', {'data': task})



@login_required(login_url='login_')
def p_delete(request, pk):
  
    try:
        task = TaskModel.objects.get(id=pk)
        task.delete() # Permanent deletion from the database
    except TaskModel.DoesNotExist:
        # Task was already deleted or doesn't exist
        pass
        
    return redirect('trash')


@login_required(login_url='login_')
def restore(request, pk):
    
    try:
        task = TaskModel.objects.get(id=pk)
        # Set the flag back to False to restore it to the Home page
        task.is_delete = False 
        task.save()
    except TaskModel.DoesNotExist:
        # Task doesn't exist, just move on
        pass
        
    # After restoring, redirect back to the Trash page
    return redirect('trash')



@login_required(login_url='login_')
def restore_all(request):
   
   
    # Filter all tasks that are currently marked as deleted
    TaskModel.objects.filter(is_delete=True).update(is_delete=False)
        
    # After restoring, redirect back to the Trash page to show it's empty
    return redirect('trash')



@login_required(login_url='login_')
def clear_all(request):
  
  
    TaskModel.objects.filter(is_delete=True).delete()
        
    return redirect('trash')