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

**Lambda Architecture | Kafka → Spark → S3 (Archive Raw) → PostgreSQL**

Repository:  
https://github.com/SangjunRyu/clinical-search-data-pipeline

---

## Overview

Designed and implemented an **end-to-end Lambda Architecture data pipeline** processing over **5.2M clinical search log events** (TripClick dataset).

The system supports:

- Daily batch analytics (T+1 consistency)
- Near real-time dashboards (5-minute micro-batch)
- Immutable raw data retention for replay & reprocessing
- Fully containerized distributed infrastructure (Docker Compose)

This project simulates a production-grade streaming + batch hybrid architecture.

---

## Architecture Summary

### Ingestion Layer
- Dual Web Servers generating event logs
- Custom Python Kafka Producers
- 3-broker Kafka Cluster (Confluent 7.5.1)
- Partitioning strategy to prevent data skew

### Batch Layer (Accuracy & Reprocessing)

Kafka  
→ `batch_to_archive_raw.py`  
→ S3 `archive_raw/` (Immutable, Parquet)  
→ `etl_to_batch_mart.py`  
→ PostgreSQL Batch Mart (T+1)

Key Characteristics:
- Immutable raw storage
- Full reprocessing capability
- Deduplication using `xxhash64(session_id|document_id|event_ts)`
- Idempotent batch execution

---

### Speed Layer (Near Real-Time Analytics)

Kafka  
→ `streaming_to_realtime_mart.py`  
→ PostgreSQL Realtime Mart

Key Characteristics:
- Spark Structured Streaming (5-minute micro-batch)
- Checkpoint-based offset management
- At-least-once processing + dedup strategy
- Real-time anomaly & trend detection

---

## Data Layers

| Layer | Storage | Purpose |
|-------|---------|----------|
| Archive Raw | AWS S3 (`archive_raw/`) | Immutable raw event storage |
| Batch Mart | PostgreSQL `mart_*` | Daily analytical marts |
| Realtime Mart | PostgreSQL `mart_realtime_*` | 5-minute micro-batch analytics |

---

## Implemented Marts

### Batch Mart (T+1)
- `mart_session_analysis`
- `mart_daily_traffic`
- `mart_clinical_areas`
- `mart_popular_documents`

### Realtime Mart (5-minute micro-batch)
- `mart_realtime_traffic_minute`
- `mart_realtime_top_docs_1h`
- `mart_realtime_clinical_trend_24h`
- `mart_realtime_anomaly_sessions`

---

## Orchestration

- Apache Airflow (2.10.5)
- Modular DAG design
- DockerOperator & SSHOperator integration
- Layer-based pipeline separation (Ingestion / Processing / Serving)

---

## Key Engineering Principles

- Lambda Architecture (Batch + Speed layer separation)
- Immutable raw storage for replayability
- Idempotent batch jobs
- Deduplication via hash-based composite keys
- Offset-controlled streaming with checkpointing
- Simplified serving layer (Direct PostgreSQL load)

---

## Tech Stack

- Apache Kafka (7.5.1)
- Apache Spark (3.4.1)
- Apache Airflow (2.10.5)
- PostgreSQL (15)
- AWS S3
- Apache Superset (3.1.0)
- Docker Compose (3.8)

---

## What This Project Demonstrates

- Distributed streaming system design
- Batch + real-time hybrid processing
- Production-style replay & reprocessing strategy
- Data modeling for analytical marts
- Full infrastructure ownership (Kafka → Spark → Orchestration → Serving)

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
