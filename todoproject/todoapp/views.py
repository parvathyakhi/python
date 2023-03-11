from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from todoapp.models import task
from django .views.generic import ListView
from django .views.generic.detail import DetailView
from django .views.generic.edit import UpdateView,DeleteView

class tasklistview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'ts'
class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'
class taskupdate(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url = reverse_lazy('cgv')
# after deletion where to go that given in success url


# Create your views here.
def todo(request):
    task1= task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        tasks=task(name=name,priority=priority,date=date)
        tasks.save()
    return render(request,'home.html',{'ts':task1})
# def detail(request):
#
#     return render(request,'detail.html',{'ts':tasks})

def delete(request,taskid):
    taskss=task.objects.get(id=taskid)
    if request.method=='POST':
        taskss.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task2=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=task2)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'t':task2})

