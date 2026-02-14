# Sangjun You

**Data Engineer | Distributed Systems | Streaming & Cloud Architecture**

Currently working as a **Data Engineer in IT Operations** at **Mirae Asset Life Insurance**, building and optimizing enterprise-scale data systems for business intelligence and operational decision-making.

I focus on:

- Designing **end-to-end data pipelines (Batch + Streaming)**
- Building **distributed systems with Kafka & Spark**
- Cloud-native architecture on **AWS**
- Production-grade BI systems for executive stakeholders
- Data modeling, performance tuning, and reliability engineering

📌 LinkedIn  
https://www.linkedin.com/in/상준-유-a29442257/

---

# 💼 Work Experience

## Mirae Asset Life Insurance — IT Operations & Data Engineer  
**Feb 2025 – Present**

### Enterprise Data Architecture & BI Engineering

- Design and maintain enterprise **data marts and DW pipelines**
- Develop and optimize **batch ETL workflows** for insurance and financial datasets
- Provide executive-level BI dashboards for C-level decision-making
- Ensure **data integrity, performance optimization, and governance compliance**
- Troubleshoot and optimize production batch jobs and database workloads

### Core Focus Areas

- Large-scale relational data modeling
- Analytical query performance tuning
- Secure data masking and access control
- Production-grade pipeline reliability

---

# 🚀 Featured Project: Clinical Search Data Pipeline

**Kafka → Spark → S3 → PostgreSQL | Lambda Architecture**

Repository:  
https://github.com/SangjunRyu/clinical-search-data-pipeline

## Overview

Designed and implemented a **production-style Lambda Architecture pipeline** processing over **5.2M clinical search log events**.

Supports:
- Batch analytics
- Real-time streaming dashboards
- Reprocessing and replay capability

Fully containerized distributed infrastructure using Docker.

---

## Architecture

### Ingestion Layer
- Apache Kafka (3-broker cluster)
- Custom Python producers
- Session-hash partitioning strategy

### Processing Layer
- Spark Structured Streaming (5-minute micro-batch)
- Spark Batch ETL jobs
- Deduplication using `xxhash64(session_id|document_id|event_ts)`

### Storage Layer
- Bronze: Raw event archive in AWS S3
- Silver: Curated & deduplicated datasets
- Gold: PostgreSQL analytical marts

### Orchestration
- Apache Airflow DAGs
- DockerOperator & SSHOperator
- Idempotent daily batch execution

---

## Data Marts Implemented

- `mart_daily_traffic`
- `mart_popular_documents`
- `mart_clinical_trend`
- `mart_realtime_traffic_minute`
- `mart_realtime_top_docs_1h`
- `mart_realtime_anomaly_sessions`

---

## Key Engineering Decisions

- Single consumer group with internal branching logic
- Exactly-once semantics via checkpoint-based offset control
- Dynamic partition overwrite strategy for S3
- Offset-based replay strategy for reprocessing
- Skew prevention via session-based partitioning

---

# ☁ Cloud Infrastructure Project: AWS 3-Tier Architecture

Repository:  
https://github.com/SangjunRyu/AWS-3tier-Architecture

Designed a scalable 3-tier architecture including:

- EC2 + Load Balancer
- Reverse Proxy (Apache)
- Prometheus & Grafana monitoring
- K6 load testing
- S3 log archiving

Validated scalability under concurrent simulated traffic.

---

# 🚒 Fire Emergency Response Data Platform

Repository:  
https://github.com/SangjunRyu/Cloud9-Final-Project

- Batch + real-time analytics on emergency response times
- AWS Glue ETL + Lambda streaming ingestion
- SNS alert integration
- Data-driven optimization of 7-minute golden-time target

---

# 🛠 Technical Stack

## Programming
Python, Java, SQL, C++

## Data Engineering
Apache Kafka  
Apache Spark (Batch & Streaming)  
Apache Airflow  
ETL Pipeline Design  
Data Modeling  
Event-Driven Architecture  

## Cloud & DevOps
AWS (EC2, S3, Lambda, Glue, IAM, VPC)  
Docker  
Kubernetes  
Prometheus  
Grafana  
CI/CD  

## Databases
PostgreSQL  
MySQL  
DynamoDB  

---

# 🎓 Education

Bachelor of Engineering  
Computer Science & Electronic Engineering  
Chung-Ang University, Seoul  
GPA: 4.21 / 4.5


## 🌍 Language Proficiency

- **TOEFL**: 89 (June 2023)
- **Exchange Program**: University of Turku, Finland (Dec 2023 – June 2024)  
  - Participated in software development and data engineering projects.

---

# 🌍 Career Objective

Seeking opportunities in:

- Global Tech Companies
- Cloud-native Data Engineering roles
- Distributed Systems & Streaming Infrastructure teams

I aim to build scalable, fault-tolerant, and intelligent data systems at global scale.
