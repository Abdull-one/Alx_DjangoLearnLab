# Social Media API

This is the backend for a simple Social Media Platform built with **Django REST Framework (DRF)**.  
The API supports user authentication and profile management.

---

## Project Setup (Task 0)

### Steps Done:
1. Created Django project: `social_media_api`
2. Installed dependencies:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt
## Task 1 – Database Models & Migrations

In this task, we defined and migrated the core models for the application.

### Implemented Features
- Created **Custom User model** by extending `AbstractUser`.
- Added `date_of_birth` and `profile_photo` fields to the User model.
- Created the following app models:
  - **Post** – Stores text/image posts from users.
  - **Comment** – Allows users to comment on posts.
  - **Like** – Lets users like/unlike posts.
- Registered apps (`accounts`, `posts`) in `INSTALLED_APPS`.
- Configured **PostgreSQL database** in `settings.py`.
- Ran initial migrations successfully.
