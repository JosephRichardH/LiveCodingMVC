from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Barang
from .forms import PostForm

# Create your views here.
def BarangPost(request):
    Barangs = Barang.objects.all()
    return render(request, 'Barang.html', {'Barangs':Barangs})

def Barang_Input(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(BarangPost)
    else:
        form = PostForm()
        return render(request, 'BarangInput.html', {'form': form})

def Barang_Detail(request, barang_id):
    Barangs = Barang.objects.get(pk=barang_id)
    return render(request, 'BarangDetail.html', {'Barangs':Barangs})
