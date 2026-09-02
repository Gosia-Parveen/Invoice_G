# Schema

Answer each of these, in your own words.

- Table by table: what columns and types does each one have?
## TABLE-1 :- Subscription table
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
- Which relationships are one-to-many, and which are many-to-many?

## one-to-many relationships:
1. User → Subscription — one user can own multiple subscriptions, while each subscription belongs to one user.
2. Subscription → Invoice — one subscription can have multiple invoices, while each invoice belongs to one subscription.
3. User → Credit Note — one user can create multiple credit notes, while each credit note is created by one user.


## one-to-one relationship:**
1. Invoice → Credit Note — one invoice can have only one credit note, and each credit note belongs to one invoice.

## many-to-many relationships:**
1. Subscription → User — one subscription can have multiple collaborators, and one user can collaborate on multiple subscriptions.


                              --------------------------------------------------------------------------------
- Which constraints are enforced by the database, and which by application code — and why did you draw the line there?

                              --------------------------------------------------------------------------------
- What did you deliberately denormalise?

                              --------------------------------------------------------------------------------
- What would break first if this had 100x the data?
