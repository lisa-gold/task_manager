from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from task_manager.labels.models import Labels
from task_manager.labels.forms import LabelForm, LabelUpdateForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect


class CustomLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = 'To open this page log in!'
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 self.permission_denied_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IndexView(CustomLoginRequiredMixin, ListView):
    model = Labels
    template_name = 'labels/index.html'


class LabelCreate(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Labels
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels:index')
    success_message = 'Label successfully added!'


class LabelUpdate(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Labels
    form_class = LabelUpdateForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels:index')
    success_message = 'Label successfully updated!'


class LabelDelete(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:index')
    success_message = 'Label successfully deleted!'
    redirect_field_name = reverse_lazy('labels:index')

    def render_to_response(self, context, **response_kwargs):
        label = super(LabelDelete, self).get_object()
        if label.tasks_set.all():
            denied_message = "Label is in use, you cannot delete it!"
            messages.warning(self.request, denied_message)
            return HttpResponseRedirect(self.redirect_field_name)
        return super().render_to_response(context, **response_kwargs)