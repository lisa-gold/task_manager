from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin


class TaskAuthor(UserPassesTestMixin):
    permission_denied_message = _("Only task's author can delete it!")

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.warning(self.request, self.permission_denied_message)
            return redirect(self.redirect_field_name)
        return super().handle_no_permission()