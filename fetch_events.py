import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime

def fetch_and_generate_calendar():
    url = "https://www.prekindle.com/events/tower-theatre"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    calendar = Calendar()

    for event_div in soup.find_all("div", class_="event-card"):
        try:
            title_tag = event_div.find("div", class_="event-title")
            date_tag = event_div.find("div", class_="event-date")
            link_tag = event_div.find("a", href=True)

            title = title_tag.text.strip() if title_tag else "Tower Theatre Event"
            date_text = date_tag.text.strip() if date_tag else None
            url = "https://www.prekindle.com" + link_tag['href'] if link_tag else None

            event_date = datetime.strptime(date_text, "%a, %b %d, %Y %I:%M %p") if date_text else None

            if event_date:
                event = Event(name=title, begin=event_date, url=url)
                calendar.events.add(event)
        except Exception as e:
            print(f"Error parsing event: {e}")

    with open("tower_theatre.ics", "w") as f:
        f.writelines(calendar)
