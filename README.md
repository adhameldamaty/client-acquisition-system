

    # 🚀 Client Acquisition System - Microservices Architecture
    
    ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
    ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    ![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
    ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
    ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
    ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
    
    A production-ready **Microservices Application** simulating a complete client acquisition workflow. This project demonstrates the evolution from simple scripts to a fully containerized, orchestrated, and monitored infrastructure.
    
    ---
    
    ## 🏗️ Architecture Overview
    
    The system is composed of decoupled services communicating via REST APIs, protected by a Reverse Proxy, and monitored in real-time.
    
    ```mermaid
    graph TD;
        User((User)) -->|HTTP Request| Frontend[Streamlit UI];
        Frontend -->|Internal Network| Nginx[Nginx Gateway];
        Nginx -->|/automation| Auto[Automation Service];
        Nginx -->|/reporting| Report[Reporting Service];
        Nginx -->|/email| Email[Email Service];
        Auto -->|Trigger| Email;
        Report -->|Read/Write| DB[(PostgreSQL)];
        Prometheus -->|Scrape Metrics| All_Services;
        Grafana -->|Visualize| Prometheus;

* * *

## 📖 Project Evolution & Design Decisions

This project was built in phases to address specific infrastructure challenges. Here is the rationale behind every step:

### Phase 1: Decoupling Logic (Microservices)

-   **Goal:** Move away from Monolithic architecture.
    
-   **Action:** Split the logic into three separate Python (FastAPI) services:
    
    1.  `email_service`: Dedicated solely to sending notifications.
        
    2.  `automation_service`: Handles the business workflow.
        
    3.  `reporting_service`: Manages data and statistics.
        
-   **Result:** Services are independent. If the Email service fails, Reporting continues to work.
    

### Phase 2: Containerization (Docker)

-   **Goal:** "It works on my machine" is not enough. We needed consistency.
    
-   **Action:** Created optimized `Dockerfiles` for each service using `python:3.9-slim` to keep images lightweight.
    
-   **Result:** The application runs identically on any environment (Dev, Test, Prod).
    

### Phase 3: Traffic Management (Nginx Gateway)

-   **Goal:** Security and Routing. We didn't want to expose every microservice port to the outside world.
    
-   **Action:** Implemented **Nginx** as a Reverse Proxy/API Gateway.
    
-   **Result:** Users communicate only with Port `8501` (Frontend) or `8080` (Gateway). Nginx internally routes traffic to the correct container (`/email`, `/automation`).
    

### Phase 4: Data Persistence (PostgreSQL & Volumes)

-   **Goal:** Retain data even if containers crash or restart.
    
-   **Action:** Integrated PostgreSQL and mapped a Docker Volume (`postgres_data`).
    
-   **Result:** Client reports are stored permanently on the host machine, ensuring zero data loss during deployments.
    

### Phase 5: Observability (Monitoring Stack)

-   **Goal:** To know the health of the system without checking logs manually.
    
-   **Action:** Deployed **Prometheus** to scrape metrics and **Grafana** to visualize them.
    
-   **Result:** A real-time dashboard showing system health and request counts.
    

### Phase 6: User Interface (Frontend)

-   **Goal:** Allow non-technical users to interact with the backend.
    
-   **Action:** Built a **Streamlit** web application.
    
-   **Result:** A user-friendly interface to trigger workflows and view live database statistics.
    

* * *

## 🧠 Challenges & Troubleshooting (DevOps Journey)

Building complex infrastructure comes with bugs. Here are the critical issues I faced and solved:

### 1\. 🛑 Nginx "Host Not Found" (Race Condition)

-   **The Issue:** The Nginx container kept crashing immediately upon startup with `Exit 1`.
    
-   **The Cause:** Nginx starts very fast. It tried to resolve the IP addresses of the upstream services (`email_service`) before Docker had finished creating the internal network for them.
    
-   **The Solution:**
    
    -   Added `depends_on` in `docker-compose.yml`.
        
    -   Crucially, added `restart: always`. This makes Nginx retry automatically until the upstream services are alive and reachable.
        

### 2\. 🔌 Legacy Docker Compatibility

-   **The Issue:** `KeyError: 'ContainerConfig'` during builds.
    
-   **The Cause:** Conflict between the legacy `docker-compose` (v1) tool and modern Docker engine metadata.
    
-   **The Solution:** Migrated fully to the modern `docker compose` (v2) CLI and performed a deep clean (`docker container prune`) to remove orphaned legacy state.
    

### 3\. 💾 SQLAlchemy Session Errors

-   **The Issue:** The API returned `Internal Server Error` and `DetachedInstanceError`.
    
-   **The Cause:** The code closed the database session (`db.close()`) _before_ the API could read the data from the object.
    
-   **The Solution:** Refactored the code to use `db.refresh(instance)` and extracted the necessary data into variables _before_ closing the session.
    

* * *

## 🚀 How to Run the Project

### Prerequisites

-   Docker Desktop or Docker Engine installed.
    
-   Git installed.
    

### Installation Steps

1.  **Clone the repository:**
    
    Bash
    
        git clone [https://github.com/adhameldamaty/client-acquisition-system.git](https://github.com/adhameldamaty/client-acquisition-system.git)
        cd client_acquisition_system
    
2.  **Build and Start the System:**
    
    Bash
    
        docker compose up --build -d
    
3.  **Access the Application:**
    
    -   **Frontend UI (The App):** [http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)
        
    -   **Grafana Dashboard:** [http://localhost:3000](https://www.google.com/search?q=http://localhost:3000) (User: `admin` / Pass: `admin`)
        
    -   **Prometheus:** [http://localhost:9090](https://www.google.com/search?q=http://localhost:9090)
        

* * *

## 📂 Project Structure

Plaintext

    client_acquisition_system/
    ├── automation_service/     # Workflow Logic
    ├── email_service/          # Notification Logic
    ├── reporting_service/      # Database Interactions
    ├── frontend/               # Streamlit User Interface
    ├── infrastructure/
    │   ├── nginx/              # Gateway Configuration
    │   └── prometheus/         # Metrics Configuration
    ├── docker-compose.yml      # Orchestration File
    └── README.md               # Documentation

* * *

**Author:** [Adham Eldamaty](https://www.google.com/search?q=https://github.com/adhameldamaty) _DevOps Engineer | Python Developer_




