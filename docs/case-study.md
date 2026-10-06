# Case Study: Private Document Automation For Expense Maps

This is a sanitized public case study for a private operational system. It excludes private source files, databases, spreadsheets, PDFs, contact details, credentials and organization-specific documents. A separate runnable demo now reproduces the generic JSON-to-XLSX pattern with invented data and a fresh implementation.

## Problem

The original workflow required preparing repeated spreadsheet-based expense maps for multiple operating units. The process involved recurring metadata, source PDFs, official templates, validation rules and manual review before delivery.

Manual preparation created risk in three areas:

- Repetitive typing across many units.
- Template drift or broken spreadsheet formatting.
- Incomplete fiscal/document fields reaching review too late.

## Solution

I built a private Python automation system with:

- A normalized SQLite data layer for unit metadata.
- A desktop app for data entry, validation, draft recovery and spreadsheet generation.
- PDF extraction helpers for invoices, payment documents and supporting files.
- OCR fallback for scanned PDFs when Tesseract is available.
- A local FastAPI web version for use on a Raspberry Pi inside the internal network.
- Packaging and setup notes for moving the project between machines.

## Architecture

![Architecture](images/architecture.svg)

The system separates sensitive operational data from reusable automation ideas:

- Private repo: source documents, database, templates, generated files and executable packaging.
- Public case study: architecture, engineering decisions, portfolio summary and safety boundary.

## Technical Highlights

- Python automation around Excel templates while preserving workbook layout.
- SQLite schema design for repeatable unit metadata.
- PDF text extraction with OCR fallback.
- GUI workflow for review before final spreadsheet generation.
- Draft autosave per unit/period.
- Local FastAPI version designed for Raspberry Pi deployment.
- Security boundary: local-network use only, no public exposure without authentication and HTTPS review.

## What I Would Reuse In A Public Demo

- Generic Excel template filling.
- Fake unit records.
- Synthetic PDFs generated only for tests.
- Validation rules as public examples.
- A small FastAPI demo with upload, preview and download.

## What Stays Private

- Real source documents.
- Real unit records and contact details.
- Fiscal documents, PDFs and generated spreadsheets.
- Credentials or historical restricted files.
- Full private repository history.

## Recruiter Takeaway

This project shows practical automation for a real business process: data modeling, document parsing, spreadsheet generation, desktop UI, local web deployment, validation and operational safety.
