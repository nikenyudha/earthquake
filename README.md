🌍 Global Earthquake Tracker
End-to-End Geospatial Data Pipeline

A real-time global earthquake monitoring system that ingests public seismic data into a cloud database and visualizes it through an interactive 3D geospatial dashboard.
This project demonstrates a complete data engineering workflow — from API ingestion to cloud storage and interactive visualization.

🚀 Key Features
🔄 Automated ETL Pipeline

Automatically fetches real-time earthquake data from the USGS (United States Geological Survey) public API in GeoJSON format.

☁️ Cloud Data Warehouse
Persistent and scalable data storage using Neon PostgreSQL (Serverless).

🛡️ Anti-Duplicate System
Implements SQL constraints with ON CONFLICT to ensure:
- Data integrity
- No duplicate records
- Efficient storage management

🌎 3D Geospatial Visualization
- Interactive 3D dashboard built with PyDeck that:
- Differentiates earthquake magnitude by color
- Represents intensity through point size
- Displays detailed tooltip information

| Category       | Technology                                 |
| -------------- | ------------------------------------------ |
| Language       | Python 3.14                                |
| Libraries      | Pandas, SQLAlchemy, PyDeck, Requests       |
| Database       | Neon PostgreSQL (Serverless)               |
| Dashboard      | Streamlit                                  |
| Infrastructure | GitHub Actions (Planned) / Local Scheduler |

## 👩‍💻 Author
**Niken Larasati**
**(Data Scientist & Writer)**
