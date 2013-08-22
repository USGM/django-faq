from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from faq.models import Topic

class FaqPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("FAQ")
    render_template = "faq_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'topics': Topic.objects.all(),
            'instance': instance,
            'placeholder': placeholder})
        return context

plugin_pool.register_plugin(FaqPlugin)
