from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import TunnelForm

@login_required
def index(request):
    return render(request, "tunnels/list.html", context = {})

@login_required
def new(request):
    if request.method == 'POST':
        form = TunnelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('list_tunnels')
    else:
        form = TunnelForm()

    return render(request, "tunnels/new.html", context={'form': form})

@login_required
def edit(request, pk=0):
    tunnel = get_object_or_404(Tunnel, pk=pk)
        
    if tunnel:
        form = TunnelForm(instance=tunnel)

        if request.method == "POST":
            form = TunnelForm(request.POST, instance=tunnel)
            if form.is_valid():
                tunnel.save()
                return redirect('list_tunnels')
            else:
                for error in form.errors:
                    HttpResponse(error)

        return render(request, 'tunnels/new.html', {'form': form})
    
    else:
        return redirect('list_tunnels')

@login_required
def remove(request, pk=0):
    tunnel = get_object_or_404(Tunnel, pk=pk)
        
    if tunnel:
        tunnel.delete()
    
    return redirect('list_tunnels')

