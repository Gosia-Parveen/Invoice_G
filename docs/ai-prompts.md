# AI prompts

The prompts you actually used, in the order you used them, grouped by what you were trying to achieve. For each significant one: what you asked, what you got back, and what you had to correct.

Include at least one prompt that produced something wrong, and what you did about it.

If you did not use AI at all, say so here, and describe your process instead.

## <What you were trying to achieve>

### Prompt

### What you got

### What you corrected


** DAY_1[30-08-02026]------------------------------------------------------------------------------

    1.
## <What you were trying to achieve>:
I was trying to understand better what the task was.

### Prompt:
We have to build a site from scratch. So this is the instruction they gave me. I want you to read it,  simplify it and explain the ten tasks they have asked me to do? Tell me in easy, what they are asking?

### What you got:
List of those ten taks in simpler words but few minor details were missing. Ai completely skiped but i wrote it in plan.

### What you corrected:
Continuely crossing with the README file to ensure i capyure maxmimum details.

                                                =======================================================
    2.
## <What you were trying to achieve>:
To add a Account Manager named Sam.

### Prompt:
give me a step by step guide to add a (user) account manager Account manager can create, edit, archive, but it cannot mark as paid, void, credit note. as mentioned it the instruction

### What you got:
Guide with simple steps to follow and add (user) Account Manger using Django Groups + Permissions,

                                                =======================================================
    3.
## <What you were trying to achieve>:
To Place the login container in the middle of the page.

### Prompt:
Fix the alignment of the html file so the login baox appears in the center.

### What you got:
Gave exact properties along with values to fix alignment.

                                                =======================================================
    4.
## <What you were trying to achieve>
        __ Admin-dashboard
Login--|__ Manager-dashboard

### Prompt
I have completed both the Account Manager dashboard and Billing Admin dashboard. Now I want you to give me step-by-step guide to form the connection from login to these dashboards.

### What you got
code for urls.py and view.py but only for Admin_dashboard.

### What you corrected
wrote code for Manager-dashboard and added along Admin_dashboard in views.py

                                                =======================================================
    5.
### Prompt
There is this bug. Even after putting correct credentials, it's not going to the dashboards.Here is the HTML form. 

### What you got
It told the post form in HTML is correct.

### What you corrected
I spotted that it was checking against username, not email address and so asked Ai to fixed in the view.py so that it will check corresponding to email IDs instead of actual username.


** DAY_2[31-08-02026]------------------------------------------------------------------------------

    1.
## <What you were trying to achieve>:
Wanted to implement login authentication so that users are required to log in before visiting any page on the website, preventing direct access to pages through the browser URL.

### Prompt:
when i type this "http://127.0.0.1:8000/admin-dashboard/" in browser it goes to dashboard without login required, apply login compulsory. give the corrected code + logout.

### What you got:
Correct code for view.py , urls.py and slight adjustment in admin dashboard.

### What you corrected:
AI initially provided a normal login setup, but I corrected it to make login compulsory, ensuring that users cannot access any page of the website without logging in first.
                                                =======================================================
    2.
## <What you were trying to achieve>:
To connect the subscription HTML with Django by creating the required model.

### Prompt:
I created the subscription HTML containing the tables with all the required columns, along with the heading and button. I want you to create the required models for it, provide the URL and view, and explain the implementation step by step.

### What you got:
A Django subscription model, URL path, and view were created to connect and display the subscription data in the HTML.

                                                =======================================================
    3.
## <What you were trying to achieve>:
A bug appeared with 404 error code, wanted to fix it. 

### Prompt:
I found a 404 error in the terminal and pasted the "error here". Fix it.

### What you got:
The AI found the issue and it was an incorrect href in the side panel. Gave the corrected code for it.

### What you corrected:
Updated the href to {% url 'admin_dash' %}, allowing the dashboard to open correctly

                                                =======================================================
    4.
## <What you were trying to achieve>
To fix the errors in the subscription HTML form (this addds new subscriptions) and make it work correctly with the Django model.

### Prompt
I found errors in the subscription HTML form and "pasted the error here" fix them according to the existing model.

### What you got:
A corrected subscription form along with the required changes in views.py and urls.py.

### What you corrected:
Fixed the subscription form, views.py, and urls.py to properly match and work with the subscription model.

                                                =======================================================
    5.
## <What you were trying to achieve>
To use the same subscription form for both adding a new subscription and editing an existing subscription.

### Prompt
I wantuse the same subscription form for both adding a new subscription and editing an existing subscription, so give a step-by-step implementation for it.

### What you got
The AI provided step-by-step changes to the URL and view, added the edit button, and explained how to test the functionality.

### What you corrected
Implemented the edit functionality so the same subscription form could be used for both adding and editing subscriptions.

                                                =======================================================
    6.
## <What you were trying to achieve>
To make the subscription form display the existing subscription details when the Edit button was selected.

### Prompt
Ran into a error the subscription form was only showing the option to add a new subscription and was not displaying the existing subscription data for editing.

### What you got
The AI modified sub.html, new_sub.html, and the input and select portions to support editing existing subscription data.

### What you corrected
Updated the form fields and template logic so that the existing subscription details could be loaded and edited using the same form.
                                                =======================================================
    7.
## <What you were trying to achieve>
Another error occurred it was preventing the edit functionality from working correctly.

### Prompt
"Pasted the bug Here", fix it.

### What you got
The AI identified a Django template language issue and provided the full corrected code.

### What you corrected
Corrected the single = sign to == for comparison in the Django template language, after which the edit functionality started working correctly.



** DAY_3[01-09-02026]------------------------------------------------------------------------------

    1.
# <What you were trying to achieve>
I created the invoice HTML and invoice form HTML for Invoice module of Billing Admin, wanted model,view and urls to connect the invoice HTML and invoice form.

### Prompt
I created the invoice HTML and invoice form HTML and require model, view, and URL path for the admin-only invoice module.

### What you got
The AI provided step by step guide for the required Django model, view, URL path, and connections for the Invoice module.

### What you corrected
Connected the Invoice HTML and form with the Django model, view, and URL for Billing Admin access.
                                                =======================================================

    2.
## <What you were trying to achieve>
To fix the error that occurred while implementing the Invoice module in script portion.

### Prompt
I encountered a bug in the Invoice.html, here {pasted the error} fix it.

### What you got
The AI identified the cause of the issue and provided the required changes to fix the Invoice.html.

### What you corrected
Applied the suggested changes and tested the Invoice.html to ensure it worked correctly for the Billing Admin.
                                                =======================================================

    3.
## <What you were trying to achieve>:
I wanted a step-by-step guide to implement the Account Manager Invoice functionality, including collaborator-based access and the read-only Credit Note column.
whlie still using the same 2 invoice htmls.

### Prompt:
To implement the Account Manager side of the Invoice module with collaborator-based access and a read-only Credit Note column, while using the same invo.html and invo_form.html for both roles.

### What you got
A step-by-step implementation guide for adding codes to specific portions in model, view, URL, and templates of Invoice for Account Manager access.

### What you corrected
Added those code in the existing model, view, URL, and templates of Invoice to support both Billing Admin and Account Manager access using the same Invoice pages.
                                                =======================================================

    4.
## <What you were trying to achieve>
To fix the Invoice form so that the Subscription field worked correctly without HTML structure errors.

### Prompt
An error has occurred in the Invoice form {here pasted the bug}, fix the issue.

### What you got
The AI identified that there were two <select> blocks for Subscription along with an extra </select> tag.

### What you corrected
Removed the duplicate Subscription <select> block and the extra </select> tag, fixing the form structure.