# 🏢 Product Multi Company

| | |
|---|---|
| **Author** | ERP Addons |
| **Website** | https://www.erp-addons.com |
| **Version** | 19.0.1.0.0 |
| **License** | OPL-1 |
| **Odoo** | 19.0 |

---

# 📖 Overview

By default, products in Odoo are generally available to all companies in a multi-company environment. In many businesses, however, certain products should only be visible or available to specific companies.

**Product Multi Company** allows you to control the visibility of each product on a company-by-company basis. Instead of creating duplicate products for different companies, you can simply choose which companies can access a product.

This helps maintain a clean product catalog while ensuring users only work with products that belong to their company.

---

# 🚀 Key Features

## 🏢 Company-wise Product Visibility

Control which companies can access a product.

**📍 Menu Navigation**

`Inventory → Products → Products`

- Assign products to one or multiple companies.
- Restrict product visibility by company.
- Keep a centralized product catalog.
- Simplify multi-company management.

---

## 📦 Better Product Organization

Use a single product database while controlling availability for each company.

This is especially useful when:

- Different companies sell different products.
- Products are available only in selected companies.
- Companies have independent product catalogs.

---

## 👀 Automatic Product Filtering

Users only see products that are assigned to their active company.

This helps:

- Reduce confusion.
- Prevent incorrect product selection.
- Improve data consistency.
- Simplify daily operations.

---

## ⚡ Easy Configuration

Company visibility can be managed directly from the Product form without changing the standard Odoo workflow.

Simply select the companies where the product should be available and save the record.

---

## 🔄 Seamless Multi-Company Integration

The module works with Odoo's built-in multi-company functionality and extends it by adding company-specific product visibility.

No changes are required to existing inventory or sales processes.

---

# ⚙️ Installation

1. Copy the **product_multi_company** module into your Odoo addons directory.
2. Update the Apps List.

**📍 Menu Navigation**

`Apps → Update Apps List`

3. Search for **Product Multi Company**.
4. Click **Install**.

---

# 📖 Usage

## 🛠️ Configure Product Companies

**📍 Menu Navigation**

`Inventory → Products → Products`

### Steps

1. Open an existing product or create a new one.
2. Navigate to the **Companies** section.
3. Select one or more companies where the product should be available.
4. Save the product.

---

## 👀 Verify Product Visibility

1. Switch to another company.
2. Open the Products menu.
3. Only products assigned to the active company will be displayed.

---

## 🏢 Manage Shared Products

If a product should be available in multiple companies:

1. Open the product.
2. Select all required companies.
3. Save the record.

The product will be visible only to those selected companies.

---

# 🏗️ Architecture

```text
product.multi.company
│
├── Product Extension
├── Company Assignment
├── Company Visibility
└── Multi-company Integration
```

---

# 📌 Changelog

## 19.0.1.0.0 — Initial Release

- Added company-wise product visibility.
- Support for multiple company assignments.
- Automatic product filtering by company.
- Seamless multi-company integration.
- Fully compatible with Odoo 19.

---

# 💬 Support

For questions, feature requests, or technical support, please visit:

🌐 **https://www.erp-addons.com**