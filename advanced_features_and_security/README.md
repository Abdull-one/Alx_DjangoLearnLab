# Permissions and Groups Setup Guide

This document explains how custom permissions and groups are configured and used in the Django project.

##  Custom Permissions

The following permissions are defined in `CustomUser` model:

- `can_view`: Allows viewing user data.
- `can_create`: Allows creating new user entries.
- `can_edit`: Allows editing existing users.
- `can_delete`: Allows deleting user accounts.

These permissions are defined in `accounts/models.py` under the `Meta` class of `CustomUser`.

---

## 👥 Groups Created (via Admin Panel)

Go to Django Admin → Groups, and create the following groups:

1. **Viewers**
   - `can_view`

2. **Editors**
   - `can_view`
   - `can_edit`
   - `can_create`

3. **Admins**
   - All permissions: `can_view`, `can_create`, `can_edit`, `can_delete`

Assign users to these groups from the Admin Panel.

---

##  View Protection

In views (e.g., in `accounts/views.py`), use permission checks like:

```python
from django.contrib.auth.decorators import permission_required

@permission_required('accounts.can_edit', raise_exception=True)
def edit_user(request):
    ...
