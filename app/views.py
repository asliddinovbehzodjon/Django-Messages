from django.shortcuts import render,redirect
from .models import Example
from django.contrib import messages
# Create your views here.
def first(request):
    if request.method=="POST":
        messages.success(request,'Malumot qoshildi!')
        item=request.POST['text']
        new=Example(item=item)
        new.save()
        return redirect('/')
    items=Example.objects.all()
    return render(request,'index.html',{'items':items})
def delete(request,id):
    messages.error(request,'Xabar ochirildi')
    Example.objects.filter(id=id).delete()
    return redirect('/')
def update(request,id):
    if request.method=="POST":
            item=request.POST['text']
            messages.info(request,'Xabar yangilandi')
            Example.objects.filter(id =id).update(item=item)
            return redirect('/')
    item=Example.objects.get(id=id)
    return render(request,'update.html',{'item':item})