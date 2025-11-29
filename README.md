The project you've developed is a comprehensive Django TODO Web Application designed to manage personal tasks and user accounts. It demonstrates a full-stack approach using the Model-View-Template (MVT) architecture.<br>
​📝<b> Project Overview</b><br>
​This application is split into two primary Django apps:<br>
​user_auth (User Authentication): Handles the security and user identity aspect of the application.
​base (Task Management): Contains the core logic for the To-Do list functionality.<br>
​🔒 User Authentication (user_auth App)<br>
​This module handles the entire user lifecycle using Django's built-in authentication system:<br>
​Login/Registration: Users can sign up for new accounts (register.html) and log in securely (login.html).<br>
​Profile Management: Users can view their profile details (username, first name, last name, email) on the profile.html page.<br>
​Password Reset: The resetpass view allows authenticated users to change their password after verifying their old one.<br>
​📋 Task Management (base App)<br>
​The base app focuses on the TaskModel, which includes fields for title, desc, and a Boolean field is_delete to manage task status.<br>
​Core Functionality (CRUD):<br>
​Home/Read: The home view displays all active tasks (is_delete=False). It also includes a search feature that queries both the task title and desc using Django's Q objects.<br>
​Add/Create: The add view handles form submission to create new tasks.<br>
​Update: The update function allows users to modify the title and description of an existing task.<br>
​Soft Deletion: The delete function implements soft deletion by setting the task's is_delete field to True instead of removing the record permanently.<br>
​Trash System (Soft Deletion Management):<br>
​Tasks marked as is_delete=True are managed in the Trash section, providing users with recovery options:<br>
​Trash View: The trash view displays only tasks where is_delete=True.<br>
​Restore: Moves an individual task back to the active list by setting is_delete=False.<br>
​Bulk Actions: Includes "restore all" and "clear all" functionality to efficiently restore all tasks or permanently delete all tasks from the trash.
