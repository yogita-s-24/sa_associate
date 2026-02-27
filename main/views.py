from django.shortcuts import render, redirect
from django.contrib import messages


# ─── Shared Data ──────────────────────────────────────────────────────────────

SERVICES = [
    {
        'title': 'Structural Consultant',
        'icon': 'fa-solid fa-drafting-compass',
        'description': 'Expert structural analysis and design for residential, commercial, and industrial buildings ensuring safety, stability, and code compliance.',
        'image': 'https://images.unsplash.com/photo-1487958449943-2429e8be8625?w=800&q=80',
        'features': [
            'Structural analysis and load calculations',
            'Seismic-resistant design',
            'Foundation design & soil-structure interaction',
            'Retaining walls and deep excavation design',
        ],
    },
    {
        'title': '2D Plan & 3D Design',
        'icon': 'fa-solid fa-ruler-combined',
        'description': 'Detailed 2D architectural plans and lifelike 3D design visualisations to help you see your project before construction begins.',
        'image': 'https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=800&q=80',
        'features': [
            'Floor plans, elevations, and section drawings',
            'Photorealistic 3D renderings and walkthroughs',
            'Site layout and landscape planning',
            'AutoCAD & BIM-based drafting',
        ],
    },
    {
        'title': 'Interior Design',
        'icon': 'fa-solid fa-couch',
        'description': 'Creative and functional interior design solutions for homes, offices, and commercial spaces that reflect your style and requirements.',
        'image': 'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=800&q=80',
        'features': [
            'Space planning and furniture layout',
            'Material, colour, and finish selection',
            'False ceiling, flooring, and lighting design',
            'Modular kitchen and wardrobe design',
        ],
    },
    {
        'title': 'Valuation',
        'icon': 'fa-solid fa-scale-balanced',
        'description': 'Professional property valuation services for residential and commercial assets, accepted by banks, courts, and government authorities.',
        'image': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80',
        'features': [
            'Residential and commercial property valuation',
            'Bank and mortgage valuation reports',
            'Stamp duty and registration valuation',
            'Legal and court-accepted valuation certificates',
        ],
    },
    {
        'title': 'Building Permission',
        'icon': 'fa-solid fa-file-signature',
        'description': 'End-to-end assistance in obtaining building permits and approvals from local municipal and government authorities.',
        'image': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800&q=80',
        'features': [
            'NA / Layout approval assistance',
            'Building plan sanction from local bodies',
            'Commencement and completion certificates',
            'Liaison with municipal and gram panchayat offices',
        ],
    },
    {
        'title': 'Supervision',
        'icon': 'fa-solid fa-helmet-safety',
        'description': 'On-site construction supervision to ensure work is executed as per approved drawings, specifications, and quality standards.',
        'image': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&q=80',
        'features': [
            'Day-to-day site monitoring and progress tracking',
            'Quality checks on materials and workmanship',
            'Coordination with contractors and labour',
            'Progress reports and documentation',
        ],
    },
    {
        'title': 'Government Contractor',
        'icon': 'fa-solid fa-landmark-dome',
        'description': 'Registered government contractor executing civil works for public infrastructure projects with full compliance to government norms.',
        'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
        'features': [
            'Roads, culverts, and drainage works',
            'Government building construction',
            'PWD and Gram Panchayat projects',
            'Tendering, billing, and documentation support',
        ],
    },
    {
        'title': 'Turnkey Project',
        'icon': 'fa-solid fa-key',
        'description': 'Complete end-to-end project execution — from design and procurement to construction and handover — delivered as a fully ready-to-use facility.',
        'image': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&q=80',
        'features': [
            'Single-point responsibility from concept to completion',
            'Design, procurement, construction & commissioning',
            'Fixed-price and fixed-timeline commitments',
            'Handover with full documentation and warranties',
        ],
    },
]

PROJECTS = [
    {
        'title': 'National Highway 48 — 4-Lane Expansion',
        'category': 'Infrastructure',
        'description': 'Widening and strengthening of a 42 km stretch of national highway including bridges and service roads.',
        'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
        'location': 'Maharashtra',
        'year': '2023',
        'value': '480 Cr',
        'status': 'Completed',
    },
    {
        'title': 'Skyline Corporate Tower',
        'category': 'Commercial',
        'description': 'A 22-floor commercial office complex with integrated parking structure and green building features.',
        'image': 'https://images.unsplash.com/photo-1486325212027-8081e485255e?w=800&q=80',
        'location': 'Pune',
        'year': '2023',
        'value': '210 Cr',
        'status': 'Completed',
    },
    {
        'title': 'River View Residential Township',
        'category': 'Residential',
        'description': '1,200 residential units across 15 towers with community amenities and landscaped open spaces.',
        'image': 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&q=80',
        'location': 'Nashik',
        'year': '2024',
        'value': '350 Cr',
        'status': 'Ongoing',
    },
    {
        'title': 'Industrial Logistics Park',
        'category': 'Industrial',
        'description': 'A 50-acre logistics and warehousing facility with heavy-duty floor loading and automated systems.',
        'image': 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800&q=80',
        'location': 'Aurangabad',
        'year': '2022',
        'value': '125 Cr',
        'status': 'Completed',
    },
    {
        'title': 'Godavari Cable-Stayed Bridge',
        'category': 'Infrastructure',
        'description': '680-metre cable-stayed bridge over the Godavari River with twin lanes and pedestrian walkways.',
        'image': 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800&q=80',
        'location': 'Nasik',
        'year': '2021',
        'value': '290 Cr',
        'status': 'Completed',
    },
    {
        'title': 'Smart City Metro Depot',
        'category': 'Infrastructure',
        'description': 'Metro rail maintenance depot with workshop, stabling lines, and administrative complex.',
        'image': 'https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=800&q=80',
        'location': 'Nagpur',
        'year': '2024',
        'value': '540 Cr',
        'status': 'Ongoing',
    },
]

CERTIFICATES = [
    {
        'title': 'ISO 9001:2015 Quality Management',
        'issuer': 'Bureau Veritas',
        'icon': 'fa-solid fa-certificate',
        'description': 'Certification validating our quality management system for design, construction, and project management services.',
        'issued': 'Jan 2020',
        'valid': 'Jan 2026',
    },
    {
        'title': 'ISO 14001:2015 Environmental Management',
        'issuer': 'Bureau Veritas',
        'icon': 'fa-solid fa-leaf',
        'description': 'Recognition of our commitment to environmental sustainability and minimising ecological impact in construction operations.',
        'issued': 'Mar 2020',
        'valid': 'Mar 2026',
    },
    {
        'title': 'OHSAS 18001 / ISO 45001 Safety',
        'issuer': 'DNV GL',
        'icon': 'fa-solid fa-shield-halved',
        'description': 'Occupational health and safety management certification demonstrating our zero-accident workplace culture.',
        'issued': 'Jun 2019',
        'valid': 'Jun 2025',
    },
    {
        'title': 'CPWD Registration — Class A Contractor',
        'issuer': 'CPWD India',
        'icon': 'fa-solid fa-landmark-dome',
        'description': 'Highest class registration with Central Public Works Department enabling participation in major government projects.',
        'issued': 'Apr 2015',
        'valid': 'Ongoing',
    },
    {
        'title': 'LEED Green Building Certified',
        'issuer': 'USGBC / IGBC',
        'icon': 'fa-solid fa-seedling',
        'description': 'Certified for designing and constructing LEED Gold and Platinum rated green buildings.',
        'issued': 'Sep 2021',
        'valid': 'Sep 2026',
    },
    {
        'title': 'BIS Certified Construction Materials',
        'issuer': 'Bureau of Indian Standards',
        'icon': 'fa-solid fa-star',
        'description': 'Bureau of Indian Standards certification for quality of construction materials and testing laboratory practices.',
        'issued': 'Feb 2018',
        'valid': 'Ongoing',
    },
]

ACCREDITATIONS = [
    {'name': 'CPWD', 'icon': 'fa-solid fa-landmark-dome'},
    {'name': 'BIS', 'icon': 'fa-solid fa-star'},
    {'name': 'IGBC', 'icon': 'fa-solid fa-seedling'},
    {'name': 'ICI', 'icon': 'fa-solid fa-helmet-safety'},
    {'name': 'NICMAR', 'icon': 'fa-solid fa-graduation-cap'},
    {'name': 'FIDIC', 'icon': 'fa-solid fa-globe'},
]

AWARDS = [
    {
        'year': '2024',
        'title': 'Best Infrastructure Project — National Level',
        'description': 'Recognised for the Godavari Cable-Stayed Bridge as the most innovative infrastructure project of the year.',
        'presenter': 'Ministry of Road Transport, India',
        'icon': 'fa-solid fa-trophy',
    },
    {
        'year': '2023',
        'title': 'Excellence in Construction Safety',
        'description': 'Zero-accident achievement across all project sites for two consecutive years, setting an industry benchmark.',
        'presenter': 'National Safety Council of India',
        'icon': 'fa-solid fa-shield-halved',
    },
    {
        'year': '2022',
        'title': 'Green Building Award — Platinum Category',
        'description': 'Skyline Corporate Tower achieved LEED Platinum, earning top recognition in sustainable construction.',
        'presenter': 'Indian Green Building Council',
        'icon': 'fa-solid fa-leaf',
    },
    {
        'year': '2021',
        'title': 'Best Civil Engineering Firm — Western India',
        'description': 'Voted the top civil engineering firm in Western India based on project delivery and client satisfaction scores.',
        'presenter': 'Indian Chamber of Commerce',
        'icon': 'fa-solid fa-award',
    },
    {
        'year': '2020',
        'title': 'Quality Excellence Award',
        'description': 'Recognised for consistently maintaining ISO 9001 standards and delivering defect-free projects.',
        'presenter': 'Quality Council of India',
        'icon': 'fa-solid fa-medal',
    },
    {
        'year': '2019',
        'title': 'Emerging Contractor of the Decade',
        'description': 'Awarded for exceptional growth from a regional firm to a nationally recognised construction company.',
        'presenter': 'Construction Industry Development Council',
        'icon': 'fa-solid fa-rocket',
    },
]

TEAM = [
    {
        'name': 'Er. Rajesh Kumar',
        'role': 'Chairman & Chief Engineer',
        'photo': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80',
        'experience': '28 Years',
    },
    {
        'name': 'Er. Priya Sharma',
        'role': 'Director — Projects',
        'photo': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&q=80',
        'experience': '20 Years',
    },
    {
        'name': 'Er. Anil Mehta',
        'role': 'Chief Structural Engineer',
        'photo': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&q=80',
        'experience': '18 Years',
    },
    {
        'name': 'Er. Sunita Patil',
        'role': 'Head — Quality & Safety',
        'photo': 'https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&q=80',
        'experience': '15 Years',
    },
]

WHY_US = [
    {'title': 'Expert Engineering Team', 'desc': '120+ licensed civil engineers and specialists with multi-domain expertise.'},
    {'title': 'ISO Certified Quality', 'desc': 'ISO 9001:2015 certified processes ensuring consistent, high-quality output.'},
    {'title': 'On-Time Delivery', 'desc': '95%+ on-time project completion rate across our portfolio.'},
    {'title': 'Safety First', 'desc': 'Zero Lost Time Incident (LTI) track record — safety is non-negotiable.'},
]


# ─── Views ────────────────────────────────────────────────────────────────────

def home(request):
    return render(request, 'home.html', {
        'services': SERVICES,
        'featured_projects': PROJECTS[:3],
        'why_us': WHY_US,
    })


def about(request):
    return render(request, 'about.html', {
        'team': TEAM,
    })


def projects(request):
    return render(request, 'projects.html', {
        'projects': PROJECTS,
    })


def services(request):
    return render(request, 'services.html', {
        'services': SERVICES,
    })


def certificates(request):
    return render(request, 'certificates.html', {
        'certificates': CERTIFICATES,
        'accreditations': ACCREDITATIONS,
    })


def awards(request):
    return render(request, 'awards.html', {
        'awards': AWARDS,
    })


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and email and subject and message_text:
            messages.success(
                request,
                f"Thank you, {name}! Your message has been received. We'll get back to you within 24 hours."
            )
        else:
            messages.error(request, "Please fill in all required fields.")

        return redirect('contact')

    return render(request, 'contact.html')
