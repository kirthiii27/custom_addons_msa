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

**Product Multi Company** allows you to control the availability of products across multiple companies in a single Odoo database.

Instead of making every product available to all companies, you can specify exactly which companies are allowed to use a particular product. This helps organizations maintain separate product catalogs for different companies while still benefiting from a shared multi-company environment.

If no company is assigned to a product, it remains available to all companies by default.

The module integrates seamlessly with Odoo's Product application and provides an easy way to manage product visibility without changing the standard workflow.

---

# 🚀 Key Features

## 🏢 Company-Specific Product Visibility

Control which companies can access each product.

**📍 Menu Navigation**

`Inventory → Products → Products`

**Features**

- Assign products to one or more companies.
- Restrict product visibility by company.
- Support shared products across multiple companies.
- Keep company-specific product catalogs organized.

---

## 📦 Flexible Product Management

Choose whether a product should be shared or company-specific.

**Benefits**

- Maintain separate product catalogs.
- Reduce product duplication.
- Simplify multi-company management.
- Improve data organization.

---

## 🌐 Shared Products

Products without any assigned companies remain available to all companies.

This provides maximum flexibility for businesses that use both shared and company-specific products.

---

## ⚡ Seamless Multi-Company Integration

The module extends the standard Product form and works naturally with Odoo's multi-company environment.

No additional workflow changes are required.

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

## 🏢 Configure Product Companies

**📍 Menu Navigation**

`Inventory → Products → Products`

### Steps

1. Open an existing product or create a new one.
2. Go to the **General Information** tab.
3. Select the companies that can use the product.
4. Save the product.

> **Note:** If no companies are selected, the product will be available to all companies.

---

## 👀 View Products by Company

When users switch to another company, they will only see:

- Products assigned to their current company.
- Shared products that are available to all companies.

This helps keep each company's product catalog clean and relevant.

---

# 🏗️ Architecture

```text
product.multi.company
│
├── Product Template Extension
├── Company Visibility Management
├── Multi-Company Product Access
└── Product Company Assignment
```

---

# 📌 Changelog

## 19.0.1.0.0 — Initial Release

- Company-specific product visibility.
- Multi-company product assignment.
- Shared product support.
- Product template extension.
- Seamless integration with Odoo multi-company environment.
- Fully compatible with Odoo 19.

---

# 💬 Support

For questions, feature requests, or technical support, please visit:

🌐 **https://www.erp-addons.com**