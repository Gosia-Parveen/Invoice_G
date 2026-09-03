# Architecture

Answer each of these, in your own words, once the system has taken real shape.

- What are the moving pieces, and how do they talk to each other?
- Where does each piece run?
## On the login page, when you enter credentials for billing admin, you go to the admin dashboard. When you put for account manager, you go to the account manager dashboard.
- What is the request path for one representative user action, end to end?
- What did you decide *not* to build, and why?



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
                                          |-Invoice                                      |-Invoice
                                          |   |-Add New                                  |  |-Add New
                                          |   |-Edit existing                            |  |-Edit existing
                                          |   |-Mark As                                  |  |-Read-only (Mark as status)
                                          |   |-Issued,Void,Paid                         |      
                                          |   |-Add Credit Note                          |
                                          |-Logout                                       |-Logout
