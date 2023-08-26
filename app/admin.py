from django.contrib import admin

from app.models import MainInfo, Features, Services, Interests, Skills, Language, Education, Partners, \
    PortfolioCategories, Portfolio, Experience, SocialNetworks

admin.site.register(
    [MainInfo, Features, Services, Interests, Skills, Language, Education, Partners, PortfolioCategories, Portfolio,
     Experience, SocialNetworks])
