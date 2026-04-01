# Citizen Grievance Tracker

A municipal complaint management platform built with React, TypeScript, and Lovable Cloud. Citizens can submit geo-tagged complaints, officers can manage assigned cases, and admins get a full analytics dashboard.

## Features

### 🏠 Citizen Portal
- **Submit Complaints** — File grievances with title, description, category, severity, and pinpoint location on an interactive map
- **My Complaints** — Track all submitted complaints with real-time status updates
- **Public Feed** — Browse and rate complaints submitted by other citizens
- **Dashboard** — Overview stats (total, pending, in-progress, resolved)

### 👮 Officer Portal
- **Assigned Complaints** — View and manage complaints assigned by admins
- **Status Updates** — Update complaint status (Pending → In Progress → Resolved)
- **Map View** — Visualize assigned complaints on an interactive map

### 🛡️ Admin Portal
- **Analytics Dashboard** — Comprehensive stats and charts for all complaints
- **User Management** — Manage citizen and officer accounts
- **Complaint Assignment** — Assign complaints to officers
- **Overdue Tracking** — Monitor unresolved complaints
- **Map Overview** — City-wide complaint heatmap

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JS |
| Styling | Tailwind CSS 3, shadcn/ui, Lucide Icons |
| Maps | Leaflet + OpenStreetMap |
| Charts | Recharts |
| Backend | Python-Flask, MySQL|

## Categories

Complaints are organized into five categories:
- 🛣️ **Road** — Potholes, broken roads, traffic issues
- 💧 **Water** — Supply issues, leakage, contamination
- 🗑️ **Garbage** — Waste collection, dumping, sanitation
- ⚡ **Electricity** — Power outages, faulty wiring, street lights
- 📋 **Others** — Miscellaneous municipal issues

## Complaint Lifecycle

```
Pending → In Progress → Resolved
```

Each complaint includes:
- Title & description
- Category & severity (1–5)
- GPS coordinates via interactive map
- Optional image upload
- Star ratings & comments from citizens

## Roles

| Role | Access |
|------|--------|
| `citizen` | Submit, track, and rate complaints |
| `officer` | Manage assigned complaints, update statuses |
| `admin` | Full access: analytics, user management, assignments |

Roles are stored in a dedicated `user_roles` table with RLS policies enforced server-side.

## Getting Started

1. Open the project in [Lovable](https://lovable.dev)
2. Sign up with an email address
3. New users default to the **citizen** role
4. Admins can promote users to **officer** or **admin** via the dashboard

## Project Structure
GRIEVANCE/
│
├── app/                     # Main Flask application package
│   ├── __pycache__/         # Compiled Python files (auto-generated)
│   │
│   ├── admin/               # Admin module (routes, logic)
│   ├── auth/                # Authentication (login, signup)
│   ├── citizen/             # Citizen-related features
│   ├── officer/             # Officer dashboard & operations
│   │
│   ├── static/              # Static files (CSS, JS, images)
│   ├── templates/           # HTML templates (Jinja2)
│   │
│   ├── __init__.py          # App factory / initialization
│   └── Utils.py             # Utility/helper functions
│
├── .vscode/                 # VS Code settings (optional)
├── .gitignore               # Git ignored files
├── README.md                # Project documentation
└── server.py                # Entry point to run Flask app

## License

Built with [Lovable](https://lovable.dev).
