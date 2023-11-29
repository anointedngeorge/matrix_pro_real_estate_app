from frontend.models import *
from matrixpro.models import *
import itertools

def groupingItem(item, group_size=3):
    container = []
    for i in range(0, len(item), group_size):
        group = item[i:i+group_size]
        container.append(group)
    return container


def getProperties():
    container = []
    m_types = MatrixPropertyType.objects.all().order_by("index")
    
    for m_type in m_types:
        propaty = MatrixProperty.objects.all().filter(property_type_id=m_type.id)
        
        if propaty.count() > 0:
            container.append({"shortname":f"{m_type.name.replace('','_')}", "name":f"{m_type.name}", "data":propaty})

    return container


def frontendContent(request):
    data = list(MatrixProperty.objects.all())
    context = {}
    context['youtube'] = YoutubeModel.objects.all().filter(is_active=True)
    context['sliders'] = Slider.objects.all().filter(is_showed=True)
    context['properties'] = getProperties()
    # context['properties'] = groupingItem(item=data)
    context['testimonials'] = groupingItem(item=list(MatriproTestimonal.objects.all().filter(control=True).order_by('created')))
    context['services'] = groupingItem(list(MatriproxServices.objects.all().order_by('index')))
    context['latest_news'] = groupingItem(
        item=list(MatriproxBlog.objects.all().filter(status=True).order_by("created")),
        group_size=2
        )

    context['settings'] = {
        'branches': [
            {'id':'lagos', 'name':'Lagos'},
            {'id':'asaba', 'name':'Asaba'},
            {'id':'head_office', 'name':'Head Office'},
        ],
        'address':[
            {'icon':'fa fa-phone', 'title':'08091647093', 'link':'','position':'left'},
            {'icon':'fa fa-map-marker', 'title':'65 North Park Bwe, USA', 'link':'','position':'left'},
            {'icon':'fa fa-envelope-o', 'title':'enugu@ceeplat.com', 'link':'','position':'left'},

            {'icon':'fa fa-user', 'title':'Email Login', 'link':'','position':'right'},
            # {'icon':'fa fa-sign-in', 'title':'Sign in', 'link':'','position':'right'},
        ],

        'about':'''
            Ceeplatprofile Ltd is a Real estate Development, Brokerage and Management 
            Company incorporated in Nigerian to provide global and best practices in real 
            estate investment services to private and portfolio investors in Nigeria and 
            around the world.
            Ceeplatprofile currently has established branch offices in Lagos, Asaba and Enugu.
        ''',

        'site_logo':'logo.png',
        'site_title':'Ceeplatprofile Ltd',
        'site_subtitle':'',

        'contacts':BranchModel.objects.all().filter(is_active=True),

        'menus': [
            {'title':'Home', 'link':'/', 'has_children':False, 'children': [
                {'title':'', 'link':''}
            ]},
            {'title':'About', 'link':'/about', 'has_children':False, 
                'children': [
                    {'title':'', 'link':''}
                ]
            },

             {'title':'Our Estates', 'link':'#', 'has_children':True, 
                'children': [{'title':prop.property_title, 'link':f'/property_detail/{prop.id}/'} for prop in MatrixProperty.objects.all() ]
            },

            {'title':'Vertican Garden Tv', 'link':'/television', 'has_children':False, 
                'children': []
            },

            {'title':'Contact', 'link':'/contact', 'has_children':False, 'children': [
                {'title':'', 'link':''}
            ]},
        ]
    }
    return context