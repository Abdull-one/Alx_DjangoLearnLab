# Security Best Practices Implemented

- DEBUG set to False for production.
- ALLOWED_HOSTS restricted to known hosts.
- CSRF and Session cookies secured over HTTPS.
- Added XSS and content sniffing protections in settings.
- All forms include {% csrf_token %}.
- Views use Django ORM instead of raw SQL queries.
- Added Content Security Policy using middleware.
