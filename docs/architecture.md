# Architecture

Answer each of these, in your own words, once the system has taken real shape.

- What are the moving pieces, and how do they talk to each other?
    ##
    -The main moving pieces of the system are the Login/Authentication, Billing Admin and Account Manager roles, Dashboards, Subscription module, Invoice module, Django models/database, and the access/permission logic.

    -When a user logs in, Django checks the credentials and role and sends the user to the respective dashboard. From the Subscription module, a Billing Admin can create a subscription by entering the customer and subscription details, including the Owner and Collaborators. This information is stored in the database through the Django models.

    -When an invoice is created for a subscription, the invoice is connected to that subscription, so the related customer and subscription information can be used while creating the invoice. The Owner and Collaborator relationship is managed through the subscription, which also controls which invoices an Account Manager can see.

    -The same data is then used by the dashboards. The Billing Admin can see all subscriptions, invoices, charts, and alerts, while an Account Manager can see only the subscriptions and invoices where they are either the Owner or Collaborator. The interface also changes according to the logged-in role, such as displaying the Account Manager's name and role, while the Billing Admin is displayed simply as Billing Admin.
-------------------------------------------------------------------------------

- Where does each piece run?
    ## 
    -On the login page, when you enter credentials for billing admin, you go to the admin dashboard. When you put for account manager, you go to the account manager dashboard.

    -The Subscription module works as follows. When a Billing Admin goes to the Subscription page, they can see all subscriptions under different customers. There is a button to add a new subscription, which opens the Subscription Form where customer and subscription details can be entered. The Billing Admin can also assign an Account Manager as the Owner and add Collaborators.

    -Moving on to Invoice, a similar pattern is followed. When a Billing Admin goes to the Invoice page, all invoices under the available subscriptions are displayed. The Billing Admin can create new invoices for the subscriptions and has the power to mark their status as Issued, Paid, or Void. The Billing Admin can also add a Credit Note when required, along with a reason for the credit note.

    -When you log in as an Account Manager, the Subscription and Invoice features follow the same general structure, but with restrictions. In the Subscription Form, the Account Manager cannot add Collaborators. The Subscription page only displays subscriptions where they are either the Owner or Collaborator. The same access logic is followed for invoices, so they can only see and create invoices for subscriptions they have access to. They cannot mark invoices as Paid, Void, or Issued.

    -The Dashboard is also different according to the role. The Billing Admin sees graphs, charts, cards, and information related to all subscriptions and invoices, whereas the Account Manager sees only information related to the subscriptions where they are the Owner or Collaborator. The Billing Admin can also dismiss overdue invoice alerts, while the Account Manager can only view the alerts.
-------------------------------------------------------------------------------

- What is the request path for one representative user action, end to end?
    ##
    -For a Billing Admin, a representative flow is:

Login → Billing Admin → Subscription → Subscription Form → Submit → Subscription stored in Database → Invoice → Invoice Form → Submit → Invoice stored in Database → Billing Admin Dashboard/Page

The Billing Admin has full access to the subscription and invoice features, including adding Collaborators, editing records, changing invoice status, and adding Credit Notes.
                            =======================
##
    -For an Account Manager, the flow is:

Login → Account Manager → Subscription → Subscription Form → Submit → Subscription/Invoice data → Invoice → Invoice Form → Submit → Account Manager

However, the Account Manager's access is restricted based on whether they are the Owner or Collaborator of the subscription. They cannot add Collaborators or change invoice status to Issued, Paid, or Void.
    -------------------------------------------------------------------------------

- What did you decide *not* to build, and why?
    ##
    -I decided not to build Generating invoices in bulk and History you cannot rewrite.*##* TASK: 7 AND 9 *##*

    -I did not completely understand these two tasks and felt that asking AI to build the entire functionality without fully understanding it would be irresponsible. I would have had to rely heavily on AI, and I would not have been able to properly recheck whether the implementation was correct.

    -The second reason was time. I had decided that the last two days would be strictly for hosting, because if the hosting did not work, the rest of the completed work would not be useful for the final submission. Because of this time limitation, I had to skip these two tasks.

If I had been given more time, I would have completed them as well.
    -------------------------------------------------------------------------------


** ## ACRCHITECTURE **

                                                           LOGIN PAGE
                                                               │
                                                       Email + Password
                                                               │
                                            ┌──────────────────┴──────────────────────┐
                                            │                                         │
                                          Billing Admin                             Account Manager
                                             │                                        │
                                             ▼                                        ▼
                                        Admin Dashboard                             AM Dashboard
                                          |-Dashboard                                    |-Dashboard
                                          |   |-4 cards Features:                        |  |-4 cards Features:        
                                          |       |-Invoice Issued                       |     |-Invoice Issued       
                                          |       |-Revenue Collected                    |      |-Revenue Collected    
                                          |       |-Overdue Invoice                      |      |-Overdue Invoice      
                                          |       |-Receive                              |      |-Receive
                                          |   |-2 Plan based chart                       |  |-2 Plan based chart        
                                          |   |-Overdue Invoice Alerts                   |  |-Overdue Invoice Alerts  
                                          |   |-Dismiss Button for alert                 |  |-Dismiss Button for alert
                                          |                                              |
                                          |-Subscription                                 |-Subscription(same for both admin+manager)
                                          |   |-Add New                                  |  |-Add New
                                          |   |-Edit existing                            |  |-Edit existing
                                          |   |-Archive/Restore                          |
                                          |-Archive Subscriptions                        |
                                          |   |-Restore                                  |
                                          |-Invoice                                      |-Invoice
                                          |   |-Add New                                  |  |-Add New
                                          |   |-Edit existing                            |  |-Edit existing
                                          |   |-Mark As                                  |  |-Read-only (Mark as status)
                                          |   |-Issued,Void,Paid                         |      
                                          |   |-Add Credit Note                          |
                                          |-Logout                                       |-Logout
