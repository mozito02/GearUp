from django.shortcuts import render
from .models import Project
from  .forms import ProjectForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# CRUD operation
def index(request):
    return render(request, 'index.html')
#Preparing the ORM
def project_list(request):
    projects=Project.objects.all()
    # order_by('-created_at')
    return render(request,'proj_list.html',{'projects':projects})
@login_required
def project_create(request):
    if request.method == 'POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=request.user
            project.save()
            return redirect('proj_list')
    else:
        form=ProjectForm()
    return render(request,'project_form.html',{'form':form})
@login_required
def project_edit(request,project_id):
    project = get_object_or_404(Project, pk=project_id,user=request.user)
    if request.method == 'POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=request.user
            project.save()
            return redirect('proj_list')
    else:
        form=ProjectForm()
    return render(request,'project_form.html',{'form':form})
@login_required
def project_delete(request,project_id):
    project = get_object_or_404(Project, pk=project_id,user=request.user)
    if  request.method == 'POST':
        project.delete()
        return redirect('proj_list')
    else:
        return render(request,'project_delete.html',{'project':project})

        
def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)
      return redirect('proj_list')
  else:
    form = UserRegistrationForm()

  return render(request, 'registration/register.html', {'form': form})