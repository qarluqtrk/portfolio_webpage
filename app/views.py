from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# class IndexView(TemplateView):
#     template_name = 'app/index.html'
from app.models import Contact, MainInfo, Features, Skills, Language, Education, Experience, Partners, Portfolio, \
    PortfolioCategories, Services, SocialNetworks


def index_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email,
                          subject=subject, message=message)
        contact.save()
        return redirect('index')
    return render(request, 'app/index.html',
                  context={
                      "main_info": MainInfo.objects.first(),
                      "features": Features.objects.all(),
                      "skills": Skills.objects.all(),
                      "languages": Language.objects.all(),
                      "educations": Education.objects.all(),
                      "experience": Experience.objects.all(),
                      "partners": Partners.objects.all(),
                      "portfolioCategories": PortfolioCategories.objects.all(),
                      "portfolios": Portfolio.objects.all(),
                      "services": Services.objects.all(),
                      "links": SocialNetworks.objects.all(),
                  })
