# Plan

Answer each of these, in your own words.

- How did you break the work into sessions?
## 
I have divided the 10 task according to the days given, so i plan on completing 2 tasks daily which means in 5 days all 10 tasks will be completed. I will have 2 days to host and test the site.
                                                        -------------------------------------------------------
- What order did you build in, and why that order?
**## Day_1: Task 1{completed}**
    Setup Django framework,
    Create Billing admin and Account Manager
    Built Login page
    ----pushed into github-----
    Built + connected Admin-Dashboard
    Built + connected Manager-Dashboard
    ----pushed into github-----

**## Day_2: Task 2-3{completed}**
    Corrected Login Authentication + Added Logout Function,
    Built + Connected Subscription Module,
    Built + Connected Subscription Form,
    Connected Add + Edit using the same Subscription Form,
    -----pushed into github-----

**## Day_3: Task 4-6{completed}**
    Built + Connected Invoice Module for billing-admin,
    Built + Connected Invoice Form for billing-admin,
    Connected Add + Edit using the same Invoice Form,
    Adding Account Manager Access using Subscription owner-based Filtering,
    Restricting Manager Invoice Actions[Credit Notes Visible to Manager but Read-only,]
    -----pushed into github-----

**## Day_4: Refining a feww details**
    Configured Account Manager Permissions for View Credit Note + Add, Change and View Invoice/Subscription,
    Restricted Credit Note Creation through Template + Backend Protection,
    Corrected Sidebar Dashboard Routing for Billing Admin + Account Managers,
    Added collaborators ManyToMany Field to Subscription,
    -----pushed into github-----
    Added features on the Admin Dashboard as required: Invoices issued, Revenue collected,
    Receivables ....Overdue Invoice Alerts + a Dismiss option for Billing Admin,
    -----pushed into github-----
 
**## Day_5: Task 8 & 10 {completed}**
    Built + Connected Account Manager Dashboard with  Added features like:
    Invoices issued, Revenue collected, Applied Owned + Collaborated Subscription and Invoice Filtering,
    Added Overdue Invoice Alerts,with Restricted Alert Dismissal for Account Managers,
    -----pushed into github-----
    Corrected Subscription page with Owner + Collaborator functionality {Restricted Invoice status actions (Issue, Paid, Void) }, and Archive support,
    Fixed and corrected Collaborator assignment at the subscription level, with Billing Admin control + restricted Account Manager access,
    Added Account Manager invoice visibility when they are either the Owner or Collaborator,
    To uniform the entire interface according to the one pattern.
    -----pushed into github-----

                                                        -------------------------------------------------------
- What did you estimate versus what it actually took?
##
I initially estimated that I could complete 2 tasks per day and finish all 10 tasks in 5 days, leaving the last 2 days strictly for hosting and testing.

The actual work took a little more time than I initially expected because some features needed rechecking, correcting, and refining after implementation. The collaboration, Owner, Archive, permissions, invoice visibility, and dashboard styling required additional changes because I found issues while testing the system. So, the basic plan was the same, but some tasks took longer because I did not want to blindly accept the first implementation without checking whether it actually matched my requirements.

                                                    --------------------------------------------------------------
- What did you cut when you ran short?
##
When I ran short on time, I decided to prioritize the core working features and hosting rather than trying to force every remaining feature into the project.

I left out Generating invoices in bulk and History you cannot rewrite. I had not completely understood these two tasks, and I did not want to depend completely on AI to build something that I would not be able to properly understand or recheck.

I also kept the last two days strictly for hosting and testing, because having a working and hosted project was more important to me than adding features at the last moment and risking the stability of the whole system.

                                                ----------------------------------------------------------------

