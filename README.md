Customer Support Triage Dashboard
Overview

This project is a lightweight internal dashboard designed to help support teams triage incoming customer messages efficiently.

The system takes a predefined list of customer support messages and automatically categorises and prioritises them. The dashboard provides a structured view, summary statistics, filtering functionality, and resolution tracking to help support leads quickly understand workload and urgency.

The goal of this project was to deliver a clean, pragmatic solution within a 24-hour build window while maintaining clarity and usability.

How to Run the Project
1. Clone the repository
git clone <repository-link>
cd support-dashboard

2. Install dependencies
python3 -m pip install -r requirements.txt

3. Run the application
python3 app.py

4. Open in browser

Visit:

http://127.0.0.1:5000

Overall Approach

Given the 24-hour constraint, I focused on:

Simplicity

Clarity

Clean execution

Delivering a complete, usable tool

I chose Flask (Python) because it allows fast backend development with minimal overhead. Server-side rendering using Jinja templates ensured simplicity and quick iteration without introducing frontend framework complexity.

The dataset is hardcoded to simulate incoming support messages, keeping the scope controlled and focused on triage logic rather than data ingestion.

The dashboard is structured into:

Summary view (category and priority breakdown)

Percentage distribution of issue types

Filterable message table

Ability to mark messages as resolved

Visual highlighting of high-priority issues

The emphasis was on usability for a support lead starting their day.

Categorisation & Prioritisation Logic

The system uses rule-based keyword matching to classify messages.

Categories

Bug → keywords such as: crash, error, not working, failed, cannot access

Billing → invoice, refund, charged, payment, subscription

Feature Request → add, feature, integration, support, export

General → fallback category for messages that do not match other patterns

Priority Assignment

High Priority

Contains urgency indicators (e.g., "urgent", "cannot access")

Critical billing issues (e.g., double charge)

Medium Priority

Standard bugs without explicit urgency

Low Priority

Feature requests and general queries

This rule-based approach was chosen because:

It is transparent and explainable

It works reliably within the scope

It avoids overengineering for a 24-hour build

Features Implemented

Summary counts by Category

Summary counts by Priority

Percentage breakdown of issue types

Filter by Category

Filter by Priority

Mark messages as Resolved

Visual highlighting of high-priority tickets

Improvements With More Time

If given more time, I would:

Replace rule-based classification with an NLP model or LLM API for smarter categorisation.

Store messages in a database (e.g., PostgreSQL) instead of in-memory storage.

Add analytics visualisations (charts for trends over time).

Add sorting by date and severity.

Add sentiment analysis to better detect frustration or urgency.

Implement user authentication and role-based access.

Add API endpoints for integration with real ticketing systems.
