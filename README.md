# Digizilla Odoo Module (Odoo v17 Community)

## Overview

The **Digizilla** module is a custom Odoo v17 Community module developed as a technical assessment task.
It provides a complete CRUD management system with multiple views, message tracking, PDF reporting, and UI customization.

The module demonstrates:

* Custom model creation
* Odoo views (Tree, Form, Kanban)
* Mail chatter integration (message & log tracking)
* JavaScript customization
* QWeb PDF reporting

---

## Technical Stack

* **Odoo Version:** 17.0 (Community)
* **Backend:** Python (Odoo ORM)
* **Frontend:** XML (Views), JavaScript
* **Reporting:** QWeb PDF

---

## Module Structure

```
digizilla/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── digizilla.py
├── views/
│   └── digizilla_views.xml
├── report/
│   ├── digizilla_report.xml
│   └── digizilla_report_template.xml
├── security/
│   └── ir.model.access.csv
├── static/
│   └── src/js/
│       └── hide_create.js
```

---

## Digizilla Model

**Model Name:** `digizilla.digizilla`

### Fields

* **Name** (Char, Required)
* **Gender** (Selection)
* **Country** (Many2one → `res.country`)
* **Joining Date** (Date)
* **Tags** (Many2many → `res.partner.category`)
* **Customers** (Many2many → `res.partner`)
* **Company** (Many2one → `res.company`, Required)
* **Notes** (Text – displayed in a separate tab)
* **Comments** (Char – displayed in a separate tab)

---

## Message Logger and Tracking

The model inherits from:

* `mail.thread`
* `mail.activity.mixin`

All main fields are tracked using `tracking=True`, enabling:

* Automatic logging of field changes
* Full message history inside the form view (chatter)

---

## Views

The module provides the following views:

* **Tree View** – List overview of Digizilla records
* **Form View** – Detailed view with:

  * Notebook tabs for Notes and Comments
  * Message chatter section
* **Kanban View** – Visual card-based layout

---

## Hide Create Button (JavaScript)

The **Create** button is hidden **only in the Form View** using JavaScript.

This is implemented by extending Odoo’s `FormController` inside:

```
static/src/js/hide_create.js
```

This approach follows best practices and meets the assessment requirement of using JavaScript instead of XML.

---

## PDF Report

A QWeb PDF report is generated for the Digizilla model.

### Report Features

* Includes all model fields
* Clean layout using `external_layout`
* Excludes message chatter and logs as requested

The report can be printed directly from the Odoo interface.

---

## Security

Access rights are defined in:

```
security/ir.model.access.csv
```

Allowing users to:

* Read
* Create
* Update
* Delete Digizilla records

---

## Installation Steps

1. Copy the `digizilla` module into your Odoo `addons` directory
2. Restart the Odoo server
3. Enable **Developer Mode**
4. Go to **Apps** → Update Apps List
5. Search for **Digizilla Management** and install

---

## Assessment Requirements Coverage

* Custom model creation
* Tree, Form, and Kanban views
* Message and log tracking
* Hide create button using JavaScript
* PDF report generation
* Clean and modular code structure

---

## Author

Developed as a technical assessment task for Odoo v17 Community.

---

If you have any questions or need further enhancements, feel free to ask.
