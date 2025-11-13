from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


# ───────────────────────────────
# หน้า Service (เพิ่มใหม่)
# ───────────────────────────────
def docs_service(request):
    """
    แสดงหน้า Service ในเมนู Docs
    """
    context = {
        'title': 'Service',
        'description': 'หน้านี้ใช้แสดงรายละเอียดบริการของเรา \U0001F496',
    }
    return render(request, 'docs/docs_service.html', context)
