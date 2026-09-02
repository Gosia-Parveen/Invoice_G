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
- Which relationships are one-to-many, and which are many-to-many?

## one-to-many relationships:
1. User → Subscription — one user can own multiple subscriptions, while each subscription belongs to one user.




                              --------------------------------------------------------------------------------
- Which constraints are enforced by the database, and which by application code — and why did you draw the line there?

                              --------------------------------------------------------------------------------
- What did you deliberately denormalise?

                              --------------------------------------------------------------------------------
- What would break first if this had 100x the data?
