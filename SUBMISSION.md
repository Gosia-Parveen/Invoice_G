# Submission

Fill this in and commit it. This is the first file we open.

## Links

- **GitHub repository:** <public repo URL> https://github.com/Gosia-Parveen/Invoice_G.git
- **Live application:** <deployed URL> https://invoice-g-bq3c.onrender.com

                                    ===================================================================================


## Notes for the reviewer

<Anything we should know before opening the link — e.g. your host sleeps when idle and the first
request can take up to a minute.>

>> The application is hosted on Render. If the site has been idle for more than 15 minutes, it may take around 2-4 minutes to wake up and from the Login page to the Dashboard or moving between pages it may take 30-40 seconds.

>> Other than this response time, I did not notice any major lag or functionality problem during my testing.

>> The website is also mobile responsive, so it can be viewed and used on both laptops and mobile phones.

>> Important: Logout of one Email_ID before Logging In with another Email_ID.

                                    ===================================================================================


## Demo credentials

|      Role       |           Email         |     Password      |
|-----------------|-------------------------|-------------------|
| Billing Admin   | bill_admin@example.com  |    bill@790       |
| Account Manager |  sam_acc@example.com    |    man_1@sam5     |
| Account Manager |  mia_acc@example.com    |    man_2@mia6     |
| Account Manager |  kaz_acc@example.com    |    man_3@kaz7     |

                                    ===================================================================================


## Stack

|  Layer   |     What you used    |              Why                          |
|----------|----------------------|-------------------------------------------|
| Frontend | Django Templates,    | To build the interface, forms, dashboards,|
|          | HTML, CSS, Bootstrap,| tables, charts, and consistent styling    |
|          | JavaScript           | directly within Django.                   |
|----------|----------------------|-------------------------------------------|
| Backend  | Django, Python       | To handle authentication, roles, views    |
|          |                      | permissions, business logic, forms, and   |
|          |                      | and communication with the database.      |
|----------|----------------------|-------------------------------------------|
| Database | PostgreSQL through   | To store the application's users,         |
|          | Supabase.            |subscriptions, invoices, credit notes, and |
|          |                      |alert information in a production database.|
|----------|----------------------|-------------------------------------------|
| Hosting  | Render               | To deploy and host the complete Django    |
|          |                      | application and make the project          |
|          |                      | accessible as a live website.             |
|----------|----------------------|-------------------------------------------|

                                    ===================================================================================


## Goal checklist

Mark each honestly. Partial is fine — say what is partial.
Done / Partial / Not done

| # |           Goal                    | Status  | Notes |
|---|-----------------------------------|---------|-------|
| 1 |   Accounts and roles              |  Done   |Completed.|
| 2 |   Subscriptions                   |  Done   |Completed.|
| 3 |   Invoices                        |  Done   |Completed.|
| 4 |   An invoice lifecycle with rules |  Done   |Completed.|
| 5 |   Collaborators                   |  Done   |Completed.|
| 6 |   Finding invoices                |  Done   |Completed.|
| 7 |   Generating invoices in bulk     | Not done|Bulk invoice generation and the required receivables CSV export were not completed because of time limitations. |
| 8 |   A dashboard                     |  Done   |Completed.|
| 9 |   History you cannot rewrite      | Not done|History you cannot rewrite were not completed because of time limitations. |
|10 |   Overdue invoice alerts          |  Done   |Completed.|

                                    ===================================================================================


## How much time did you actually spend?

>> I initially given 12 hours to complete all 10 tasks, but the project actually took 5 additional hours, so I would say I spent approximately 17 hours in total.

>> Some of the extra time went into rechecking the implementation, finding mistakes in the collaboration, Owner, archival and permission logic, correcting them according to my actual requirements, refining the interface, testing different users, and finally deploying and testing the live application.

                                    ===================================================================================


## What would you do next, with another 12 hours?

>> With another 12 hours, the first things I would complete are the two tasks I was not able to finish: bulk invoice generation and the history timeline.

>> After completing those, I would add a small communication or alerting feature between an Owner and Collaborator. For example, if a subscription has one Owner and one Collaborator and both can create invoices, there should be a way for them to check whether an invoice for a particular month has already been created. This could help prevent the same company from receiving two invoices for the same month because both users created one without knowing about the other's action.

>> I would also use the remaining time for more testing, refinement, and a few additional features if time allowed.

                                    ===================================================================================


## What are you least happy with in this codebase, and why?

>> The part I am least happy with is that I was not able to complete Task 7 and Task 9, which were the bulk invoice generation and history timeline.

>> I was particularly unhappy about this because I wanted to complete all the tasks rather than leave two unfinished. I also did not want to blindly ask AI to build these two features when I did not completely understand them myself, because I would not have been able to properly recheck whether the implementation was actually correct.

>> Apart from those two incomplete features, I am reasonably satisfied with the final result. I repeatedly rechecked the work, especially when I found problems in the AI-generated structure around collaboration, ownership, archiving, permissions, and some of the design. I corrected those parts according to my actual requirements instead of simply accepting what AI gave me.

                                    ===================================================================================
