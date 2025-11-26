.. _`Troubleshooting`:

Troubleshooting
===============
This section describes some common issues that can arise and possible solutions.

Issue #1
--------
**Protecting sensitive information (Lab 3)** 
When creating the `.env` file to store database credentials, it is critical **not to check it into Git**. Ensuring the `.env` file is listed in `.gitignore` prevents accidentally exposing passwords or other sensitive data.


Issue #2
--------
 **Case sensitivity in Flask routes (Lab 5)** 
Flask routing is **case-sensitive**, so mismatched letter casing in route definitions or URLs can cause pages to fail to load. Double-check route names and links to ensure they match exactly.

Issue #3
--------
**Proper Flask routing and navigation** 
 Incorrect routing can prevent your application from responding as expected. Always verify that route functions, templates, and navigation links are properly defined and consistent with the URLs used in your app.