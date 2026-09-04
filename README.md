# Invoice_G

Invoice_G is a **Django-based subscription and invoice management system** designed to manage customers, subscriptions, invoices, payments, credit notes, and billing information.

The application is **mobile responsive** and is deployed as a live web application using **Render**.

## Features

* Subscription management
* Invoice creation and management
* Invoice status tracking: Draft, Issued, Paid, and Void
* Credit note management
* Archive and restore subscriptions
* Dashboard with billing and revenue information
* Overdue invoice alerts
* Role-based access and permissions
* Mobile-responsive interface

## User Roles

### Billing Admin

* Full access to subscriptions and invoices
* Create, edit, archive, and restore subscriptions
* Manage owners and collaborators
* Manage invoice status
* Create credit notes
* View billing dashboards and alerts

### Account Manager

* Create and manage permitted subscriptions
* View subscriptions they own or collaborate on
* View relevant invoices
* Restricted from administrative billing actions

The project currently includes **three Account Manager users**.

## Technology

* Python
* Django
* HTML
* CSS
* Bootstrap
* JavaScript
* Chart.js
* PostgreSQL through Supabase.
* Render

## Live Application

The application is deployed on **Render** and can be accessed through the live deployment link provided above.

> **Note:** Since the application is hosted on Render, the first request may take some time if the service has been idle.

## Purpose

This project demonstrates a complete Django web application with **authentication, role-based permissions, subscription management, invoice management, dashboards, responsive design, and cloud deployment**.
