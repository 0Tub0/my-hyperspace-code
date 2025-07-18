from services.models import Service

from django.shortcuts import render

def index(request):
    static_content = """
        <div class="inner">
            <h1>Hyperspace</h1>
            <p>Just another fine responsive site template designed by <a href="http://html5up.net">HTML5 UP</a><br />
            and released for free under the <a href="http://html5up.net/license">Creative Commons</a>.</p>
            <ul class="actions">
                <li><a href="#one" class="button scrolly">Learn more</a></li>
            </ul>
        </div>
    """
    featured_services = Service.objects.filter(is_featured=True)

    context = {
        "static_content": static_content,
        "featured_services": featured_services
    }

    return render(request, 'core/index.html', context)

