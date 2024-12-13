from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Project, Region, Product
from datetime import date, timedelta
import os


def DBhome(request, project_slug=None):
    first = request.session['first']
    SuperUser = request.session['SuperUser']
    language = request.session['language']
    project = None
    region = None
    projects = Project.objects.all()
    regions = Region.objects.filter(available=True)
    products = []
    products = Product.objects.filter(available=True)
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug)
        regions = regions.filter(project=project)
        for prod in products:
            if prod.region in regions:
                region = prod.region
    language = request.session['language']
    user_name = request.session['user_name']
    SuperUser = request.session['SuperUser']
    client_domain = request.session['client_domain']
    if SuperUser:
        print('admin -->', SuperUser)
    if project:
        print('project -->', project)
    if products:
        print('products -->', products)
    if user_name and not SuperUser:
        print('client -->', user_name)
    print("region", region)
    print("regions", regions)
    return render(request, "homepage.html", {"first": first, "admin_user": SuperUser, 'project': project,
                                             'projects': projects, 'region': region, 'regions': regions,
                                             'products': products, "client": user_name, "client_domain": client_domain,
                                             "lan": language,
                                             })


def region_list(request, project_slug=None):
    project = None
    region = None
    projects = Project.objects.all()
    regions = Region.objects.filter(available=True)
    products = Product.objects.filter(available=True)
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug)
        regions = regions.filter(project=project)
        for prod in products:
            if prod.region in regions:
                region = prod.region
                products = products.filter(region=region)
    print('project', project)
    print('projects', projects)
    print('regions', regions)
    print('products', products)
    print('region', region)
    return render(request, 'list.html', {'project': project, 'projects': projects, 'region': region, 'regions': regions,
                                         'products': products})


def region_detail(request, id, slug):
    region = get_object_or_404(Region, id=id, slug=slug, available=True)
    pro_available = Product.objects.filter(available=True)
    pro_region = Product.objects.filter(region=region)
    print('region', region)
    print('available', pro_available)
    print('region', pro_region)
    language = request.session['language']
    user_name = request.session['user_name']
    return render(request, 'detail.html',
                  {'region': region, 'pro_available': pro_available, 'pro_region': pro_region, "lan": language,
                   "client": user_name})


def product_detail(request, region, slug, id):
    product = get_object_or_404(Product, region=region, slug=slug, id=id, available=True)
    print('product', product.region.project)
    language = request.session['language']
    user_name = request.session['user_name']
    return render(request, 'detail.html', {'product': product, "lan": language, "client": user_name})


# def product_catalog(request, project_slug=None):
#     project = None
#     region = None
#     projects = Project.objects.all()
#     regions = Region.objects.filter(available=True)
#     products = []
#     products = Product.objects.filter(available=True)
#     if project_slug:
#         project = get_object_or_404(Project, slug=project_slug)
#         regions = regions.filter(project=project)
#         for prod in products:
#             if prod.region in regions:
#                 region = prod.region
#     print('project', project)
#     print('projects', projects)
#     print('regions', regions)
#     print('products', products)
#     language = request.session['language']
#     user_name = request.session['user_name']
#     SuperUser = request.session['SuperUser']
#     client_domain = request.session['client_domain']
#     date_before = date.today() - timedelta(days=7)
#     client_user = request.POST.get('client_user')
#     print('client_user', client_user)
#     if client_user or SuperUser:
#         print('suser -->')
#         return render(request, 'region_projects.html', {'project': project, 'projects': projects, 'region': region,
#                                                         'regions': regions, 'products': products, "lan": language,
#                                                         'date_lim': date_before, "client": user_name})
#     else:
#         print('client_user 2nd -->', client_domain)
#         return render(request, 'region_projects.html', {'project': project, 'projects': projects, 'region': region,
#                                                         'regions': regions, 'products': products, "lan": language,
#                                                         'date_lim': date_before, "client": user_name,
#                                                         "client_domain": client_domain})


def secondHome(request):
    language = request.session['language']
    language_2 = request.POST.get('language')
    if language_2:
        language = language_2
        request.session['language'] = language
    SuperUser = None
    user_name = None
    client_domain = None
    user_name = request.session['user_name']
    SuperUser = request.session['SuperUser']
    client_domain = request.session['client_domain']
    print(user_name)
    print(SuperUser)
    print(client_domain)
    if language == 'FR':
        return render(request, "home_fr.html",
                      {"admin_user": SuperUser, "client": user_name, "client_domain": client_domain, "lan": language})
    else:
        return render(request, "region_projects.html",
                      {"admin_user": SuperUser, "client": user_name, "client_domain": client_domain, "lan": language})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/download')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

