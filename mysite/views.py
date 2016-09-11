from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View

from .models import Contact


class SubmitContact(View):

    def __init__(self):
        self.context = {}
        self.template_name = 'contact_us.html'
        super(SubmitContact, self).__init__()

    def post(self, request, *args, **kwargs):
        try:
            contact = Contact(name=request.POST.get('name'),
                              email=request.POST.get('email'),
                              phone=request.POST.get('phone'),
                              message=request.POST.get('message'))
            contact.save()
            success = True
        except:
            success = False
        self.context.update({
            'success': success,
            'message': "Your contact request has been sent successfully",
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))
