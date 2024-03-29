from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from task_manager.users.models import CustomUser
from task_manager.users.forms import UserForm
from task_manager.users.mixins import CanSelfManageObject, CanObjectBeDeleted
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin
from django.utils.translation import gettext_lazy as _


class IndexView(ListView):
    model = CustomUser
    template_name = 'users/index.html'


class UserCreate(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Registration'),
        'btn_text': _('Sign up'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('login')
    success_message = _('Successfully registered!')


class UserUpdate(SuccessMessageMixin,
                 CustomLoginRequiredMixin,
                 CanSelfManageObject,
                 UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Edit user'),
        'btn_text': _('Update'),
        'btn_class': 'btn-primary'}
    success_message = _('Successfully updated!')
    success_url = reverse_lazy('users:index')
    permission_denied_message = _("You cannot edit other users!")


class UserDelete(SuccessMessageMixin,
                 CustomLoginRequiredMixin,
                 CanSelfManageObject,
                 CanObjectBeDeleted,
                 DeleteView):
    model = CustomUser
    template_name = 'form.html'
    extra_context = {
        'title': _('Delete user'),
        'btn_text': _('Yes, delete'),
        'btn_class': 'btn-danger'}
    success_message = _('Successfully deleted!')
    success_url = reverse_lazy('users:index')
    permission_denied_message = _("You cannot delete other users!")

    def dispatch(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return CustomLoginRequiredMixin.handle_no_permission(self)
        if not CanSelfManageObject.test_func(self):
            return CanSelfManageObject.handle_no_permission(self)
        if not CanObjectBeDeleted.test_func(self):
            return CanObjectBeDeleted.handle_no_permission(self)
        return super().dispatch(context, **response_kwargs)
