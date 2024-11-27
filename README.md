# Sport Calendar

A web-based application to manage and browse sports events. The Sport Calendar allows users to create and view events, ensuring no scheduling conflicts occur between teams or venues. While the application is designed for administrators, all users currently have administrative privileges due to the lack of a login/registration feature.

---

## Features

- **Create New Events by specifying:**
  - Name
  - Description
  - Sport
  - Venue
  - Home and Away-team
  - Date and Time
  
  all these details are required to create a valid event.
- **Conflict Prevention:** Events cannot be created if there are conflicts (e.g., a team is already scheduled for a different event at the same time).
- **Browse Events:** Users can view a list of all events and search for specific ones of interest.
- **Management Tools:** Manage sports, teams, countries, and venues to ensure an organized event creation process.

---

## Table of Contents
1. [About](#about)
2. [Installation](#installation)

---

## About

Sport Calendar is designed for sports event organizers and administrators to plan events efficiently while avoiding scheduling conflicts. Although designed with administrative use in mind, the absence of authentication means all users can currently manage and create events. 

---

## Installation

### Requirements:
- Docker: https://docs.docker.com/get-started/get-docker/

<br>
To set up the Sport Calendar locally, follow these steps:

1. **Clone the repository and run make inside the dir:**
   ```bash
   git clone git@github.com:SuQuoc/sport_events_calendar.git
   cd sport_events_calendar
   make
   ```

2. **Access the application:**
Open your browser and go to http://localhost:8000
