# Decisions

Log the decisions that actually shaped this codebase — the ones where a real alternative existed and
you picked one. At least five entries. For each: what you chose, what you rejected, and why. At least
one entry must be a decision you later reversed — say what changed your mind. It can be any entry
below, not necessarily the last one; add a **Later reversed:** line to whichever one it is.

## Decision 1

- **Chose:** Check Authentication in Login page against email addresses of users.
- **Rejected:** Instead of using usernames of the users.
- **Why:** Because multiple users can have same names.
                                              ---------------------------------------------------------

## Decision 2

- **Chose:** That login should be a necessity to visit any of the webpages her.
- **Rejected:** That u can visit any page directly form the browser(by typing: /admin-dash/, /subs-form/)
- **Why:** It made login using different IDs irrelevant, Manager can visit admin dashboard from the browser.
                                              ---------------------------------------------------------

## Decision 3

- **Chose:**To use the same subscription form for both adding new entry and editing existing one. And both Admin and manager use the same form as both had same power regarding subscriptions.
- **Rejected:**To build multiple html pages for adding new, editing existing entry, different for Admin and different for manager.
- **Why:** because it wastes time, space and energy. Makes the file over crowded.
                                              ---------------------------------------------------------

## Decision 4

- **Chose:** To use the same invoice form and invoice page for both Admin and Manager. Admin will have access to mark the status as Draft, Paid, or Void and add Credit Note. Manager will not have these permissions, but will be able to see the Credit Notes and Draft status made by the Admin. The Credit Note column will be disabled for the Manager.
- **Rejected:** To build separate invoice forms and pages for Admin and Manager.  To give access power according to roles.
- **Why:** because it wastes time, space and energy. Makes the file over crowded.  And as the no. of files increase it increase the complexity of the project.

## Decision 5

- **Chose:** To make the user name/role change according to the current logged-in user dynamically, such as Billing Admin, Account Manager (Sam, Mia, Kaz....).
- **Rejected:** To hardcode Billing_Admin instead of using the current logged-in user's name/role.
- **Why:** To give a personal touch because different users will be using the system, so it should change according to the current logged-in user.
                                              ---------------------------------------------------------

## Decision 6

- **Chose:** To add two more Account Managers and one Billing Admin along with some data because it looks empty. Create at least five new subscriptions, and each subscription should have at least two to three invoices, because we need to check the working of the site till now.
- **Rejected:** To continue testing with only the existing managers, subscriptions, and invoices.
- **Why:** because we need enough data to check the working of the site till now and adding multiple managers gave it a bit of realistic effect.
