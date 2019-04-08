
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import EmpInfo
from .forms import InfoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
        
@login_required(login_url='/registrations/login/')
def info_list(request):
    infos = EmpInfo.objects.all()
    return render(request, 'empInfo/info_list.html', {'infos': infos})

@login_required(login_url='/accounts/login/')
def info_detail(request, pk):
    info = get_object_or_404(EmpInfo, pk=pk)
    return render(request, 'empInfo/info_detail.html', {'info': info})

@login_required(login_url='/accounts/login/')
def add_new(request):
    form = InfoForm(request.POST)
    if form.is_valid():
        info = form.save(commit=False)
        # info.firstName = request.user
        # info.lastName = request.user
        # info.email = request.user
        # info.mobileNumber = request.user
        # info.salary = request.user
        info.save()
        return redirect('info_detail', pk=info.pk)
    else:
        form = InfoForm()
    return render(request, 'empInfo/info_edit.html', {'form': form})

@login_required(login_url='/accounts/login/')
def info_edit(request, pk):
    info = get_object_or_404(EmpInfo, pk=pk)
    if request.method == "POST":
        form = InfoForm(request.POST, instance=info)
        if form.is_valid():
            info = form.save(commit=False)
            # info.firstName = request.user
            # info.lastName = request.user
            # info.email = request.user
            # info.mobileNumber = request.user
            # info.salary = request.user
            info.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = InfoForm(instance=info)
    return render(request, 'empInfo/info_edit.html', {'form': form})

@login_required(login_url='/accounts/login/')
def info_delete(request,pk):
    object = get_object_or_404(EmpInfo, pk=pk)
    object.delete()  
    return redirect('info_list') 

def logout_view(request):
    logout(request)
    return redirect('info_list')
