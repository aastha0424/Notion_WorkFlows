from notion_client import Client
import os
TOKEN = TOKEN = os.getenv("NOTION_TOKEN")

DATA_SOURCE_ID = "ac4020b3-ded0-8333-b477-07dc0f831044"

notion = Client(auth=TOKEN)

response = notion.data_sources.query(
    data_source_id=DATA_SOURCE_ID
)

for page in response["results"]:

    notion.pages.update(
        page_id=page["id"],
        properties={
            "Mon": {"checkbox": False},
            "Tue": {"checkbox": False},
            "Wed": {"checkbox": False},
            "Thu": {"checkbox": False},
            "Fri": {"checkbox": False},
            "Sat": {"checkbox": False},
            "Sun": {"checkbox": False},
        }
    )

    print("Reset:", page["id"])

print("Weekly reset completed.")