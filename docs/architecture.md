# Architecture

Answer each of these, in your own words, once the system has taken real shape.

- What are the moving pieces, and how do they talk to each other?
- Where does each piece run?
## On the login page, when you enter credentials for billing admin, you go to the admin dashboard. When you put for account manager, you go to the account manager dashboard.
- What is the request path for one representative user action, end to end?
- What did you decide *not* to build, and why?


DAY_1[30-08-2026]----------------------------------

                                                           LOGIN PAGE
                                                               │
                                                       Email + Password
                                                               │
                                                  ┌────────────┴──────────────┐
                                                  │                           │
                                                Billing Admin               Account Manager
                                                   │                          │
                                                   ▼                          ▼
                                                Admin Dashboard               AM Dashboard
                                                  |-Home                        |-Home
                                                  |-Subscription                |-Subscription(same for both admin+manager)
                                                      |-Add New                     |-Add New
                                                      |-Edit existing               |-Edit existing
                                                      |-Archive/Restore             |-Archive/Restore
                                                  |-Invoice                     |-Invoice
