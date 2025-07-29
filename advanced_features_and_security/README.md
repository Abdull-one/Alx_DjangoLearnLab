## Permissions & Groups Setup

### Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: `can_view`
- Editors: `can_view`, `can_create`, `can_edit`
- Admins: All permissions

### Notes
- Permissions enforced in views using `@permission_required`.
- Managed via Django Admin interface.
