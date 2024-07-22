from django.shortcuts import render, redirect, get_object_or_404
from .forms import DetailForm
from .models import Detail
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

# Create your views here.
def index(request):
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = DetailForm()         
    return render(request, "pdf/details.html", {"form": form})

def resume(request, id):
    detail = get_object_or_404(Detail, id=id)
    template = loader.get_template("pdf/resume.html")
    html = template.render({"detail":detail})
    options = {
        "page-size":"letter",
        "encoding": "UTF-8"
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment"
    filename = "resume.pdf"
    
    return response

class ResumeList(ListView):
    template_name = "pdf/resume_list.html"
    model = Detail
    context_object_name = "details"
