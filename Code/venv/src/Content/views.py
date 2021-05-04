from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def doc_view(request):
    return redirect("https://docs.google.com/document/d/1chmmfWFlP5Hf5uhSkZ_u31DODUu3Trtp4VTlmLdkvDQ/edit")
