# Schema

Answer each of these, in your own words.

- Table by table: what columns and types does each one have?
**## TABLE-1 :- Subscription table**
    id – AutoField (Primary Key)
    customer_name – CharField
    billing_email – EmailField
    plan – CharField
    billing_cycle – CharField
    price – DecimalField
    start_date – DateField
    owner – ForeignKey (User)
    is_archived – BooleanField

                          --------------------------------------------------------------------------------
**## TABLE-2 :- Invoice table**
    id – AutoField (Primary Key)
    subscription – ForeignKey (Subscription)
    invoice_number – CharField
    billing_period_start – DateField
    billing_period_end – DateField
    amount – DecimalField
    due_date – DateField
    status – CharField
    void_reason – TextField
    created_at – DateTimeField
    updated_at – DateTimeField

                          --------------------------------------------------------------------------------
**## TABLE-3 :- Credit Note table**
    id – AutoField (Primary Key)
    invoice – OneToOneField (Invoice)
    amount – DecimalField
    reason – TextField
    created_by – ForeignKey (User)
    created_at – DateTimeField

                              --------------------------------------------------------------------------------
### **TABLE-4 :- Invoice Alert Dismissal table**

    id – AutoField (Primary Key)
    invoice – ForeignKey (Invoice)
    dismissed_at – DateTimeField
    dismissed_by – ForeignKey (User)

                                ==================================================================================

- Which relationships are one-to-many, and which are many-to-many?

## one-to-many relationships:
1. User → Subscription — one user can own multiple subscriptions, while each subscription belongs to one user.
2. Subscription → Invoice — one subscription can have multiple invoices, while each invoice belongs to one subscription.
3. User → Credit Note — one user can create multiple credit notes, while each credit note is created by one user.
4. Invoice → InvoiceAlertDismissal
5. User → InvoiceAlertDismissal

## one-to-one relationship:**
1. Invoice → Credit Note — one invoice can have only one credit note, and each credit note belongs to one invoice.

## many-to-many relationships:**
1. Subscription → User — one subscription can have multiple collaborators, and one user can collaborate on multiple subscriptions.

                                ==================================================================================

- Which constraints are enforced by the database, and which by application code — and why did you draw the line there?
**##**
    -The database handles the basic structure and integrity of the data. For example, Primary Keys, Foreign Keys, One-to-One relationships, required fields, field types, unique invoice numbers, and the relationship between Subscription, Invoice, Credit Note, and User are handled through the Django models and database.

    -The application code handles the rules that depend on who is logged in and what that person is allowed to do. For example, a Billing Admin can change invoice status, add collaborators, and add Credit Notes, while an Account Manager cannot. The application also checks whether an Account Manager is the Owner or Collaborator before showing the related subscriptions and invoices.

    -I kept this separation because the database should make sure the data itself is valid, while the application should decide what each type of user is allowed to do with that data.
                                ==================================================================================

- What did you deliberately denormalise?
**##**
    -I did not deliberately denormalise any major part of the database. For this project, I preferred keeping the structure simple.

    -I kept the data separated into Subscription, Invoice, Credit Note, and Invoice Alert Dismissal tables instead of storing the same information repeatedly. For example, the invoice is connected to the Subscription through a ForeignKey, so I did not store all the subscription details again inside the Invoice table.

    -The Collaborator relationship is also kept separately through the many-to-many relationship rather than copying collaborator information into every invoice.
                                ==================================================================================

- What would break first if this had 100x the data?
**##**
    -If the system had 100 times more data, I think the dashboard and listing pages would be the first areas to face problems. 

    -At the moment, the dashboards calculate things such as invoice counts, revenue, overdue invoices, and plan-based information from the available records. With a much larger amount of data, these queries and calculations could become slower, especially when loading large Subscription and Invoice lists.

    -The next issue would probably be the large number of records displayed on the Subscription and Invoice pages. I would then need to improve the queries, add pagination, use better database indexing where required, and optimize the dashboard calculations.

    -I kept the implementation reasonably simple rather than designing it for a very large production-scale dataset.  
                                ==================================================================================
