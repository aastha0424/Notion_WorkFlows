# Notion Weekly Habit Reset

Automatically reset weekly habit-tracking checkboxes in a Notion database every Sunday using the Notion API and GitHub Actions.

## Features

* Automatically resets habit checkboxes every week
* Uses the official Notion API
* Runs on GitHub Actions (no server required)
* Secure authentication using GitHub Secrets
* Fully automated and free to run

## Tech Stack

* Python 3.11
* Notion API
* GitHub Actions
* notion-client

## Project Structure

```text
.
├── .github
│   └── workflows
│       └── reset.yml
├── reset.py
├── requirements.txt
└── README.md
```

## How It Works

1. Connect a Notion Integration to your habit-tracking database.
2. The Python script queries all habit entries from the Notion data source.
3. Every weekly checkbox property (Mon–Sun) is reset to `False`.
4. GitHub Actions runs the script automatically every Sunday.

## Database Structure

The database contains the following properties:

| Property | Type     |
| -------- | -------- |
| Name     | Title    |
| Mon      | Checkbox |
| Tue      | Checkbox |
| Wed      | Checkbox |
| Thu      | Checkbox |
| Fri      | Checkbox |
| Sat      | Checkbox |
| Sun      | Checkbox |

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Notion_WorkFlows.git
cd Notion_WorkFlows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variable

Create a GitHub Secret:

```text
NOTION_TOKEN
```

with your Notion Integration Token.

### 4. Connect Notion Integration

Share the habit-tracking database with your Notion Integration and grant edit permissions.

## Running Locally

```bash
python reset.py
```

Expected output:

```text
Reset: <page_id>
Reset: <page_id>
...
Weekly reset completed.
```

## GitHub Actions Automation

The workflow runs automatically every Sunday using:

```yaml
schedule:
  - cron: '0 0 * * 0'
```

A manual trigger is also available through:

```text
Actions → Weekly Habit Reset → Run Workflow
```

## Future Improvements

* Monthly habit analytics
* Streak tracking
* Completion percentage dashboard
* Email/Discord notifications
* Multi-database support
* Custom reset schedules

## Why I Built This

I wanted a lightweight, fully automated habit-tracking system in Notion without manually resetting weekly checklists. This project demonstrates API integration, workflow automation, authentication, and cloud-based scheduled execution using GitHub Actions.

## License

MIT License
