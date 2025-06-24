from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm

def index(request):
    messages = Message.objects.all()
    return render(request, 'index.html', {'messages': messages})

def post(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        Message.objects.create(content=content)
        return redirect('index')
    return render(request, 'post.html')

def post1(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        Message.objects.create(content=content)
        return redirect('index')
    return render(request, 'post1.html')

def post2(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content:
            Message.objects.create(content=content)
            return redirect('index')
    return render(request, 'post2.html')

def postform(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MessageForm()
    return render(request, 'postform.html', {'form': form})

def delete(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()
    return redirect('index')
