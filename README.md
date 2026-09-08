# Sangjun You

**Data Engineer | Distributed Systems | Streaming & Cloud Architecture**

Data Engineer with production experience across two companies — enterprise DW/BI pipelines at a life insurance company, and **Spark/Delta advertising data pipelines** at a performance marketing agency, where I focused on execution-plan-level performance analysis and regression-safe data changes.

I focus on:

- Designing **end-to-end data pipelines (Batch + Streaming)**
- Building **distributed systems with Kafka & Spark**
- **Spark execution-plan analysis and executor-level profiling**
- Cloud-native architecture on **AWS**
- Production-grade BI systems for executive stakeholders
- Data modeling, performance tuning, and reliability engineering

📌 LinkedIn  
https://www.linkedin.com/in/sangjun-you-a29442257/

---

# 💼 Work Experience

## Echo Marketing — Data Engineer (Contract)  
**Jun 2026 – Sep 2026**

Owned the **gold layer and BI serving layer** of an advertising data platform on Databricks
(PySpark / Delta Lake / Unity Catalog), serving 20+ advertiser accounts.
Upstream ingestion through the silver layer was owned by a separate platform cell.

### Production Pipeline Optimization

- Optimized the URL classification stage of a **24.5M-row batch**. Read the generated plan
  (`explain codegen`) and found that regex predicates (`rlike`) were **not** rewritten into
  cheap `Contains` operations, unlike `like` — so cost scaled with how often the regex engine ran,
  not with the number of conditions
- Measured actual traffic distribution (**71% / 27.5% / 3%**) and **reordered branch conditions by
  frequency**, then added cheap string pre-checks so regex evaluation short-circuits for most rows
- Profiled the vectorized-UDF alternative on executors: of **763s** total, **string lowercasing
  accounted for 25%** — not regex, which **disproved my initial hypothesis**. Kept the native Spark
  implementation rather than the UDF path
- Rejected a direct runtime comparison between the two implementations after finding their
  **IO cache hit ratios differed (2.21% vs 37.59%)**
- **Verified row-level equivalence before release** — full-set comparison surfaced **1,581
  misclassified rows introduced by my own new logic**; fixed and confirmed zero difference
  in both directions. **Shipped to production and running as validated.**

### Query Load Attribution & Serving Performance

- Attributed peak-hour report-refresh contention on a shared SQL warehouse to **three layers**:
  fixed compute size, schedule clustering on the hour/half-hour, and long session occupancy
  by large result transfers
- Broke the load down **per account** instead of in aggregate — surfaced duplicate query issuance
  by a BI client (**5–9 identical queries per day**, up to **35 concurrent sessions**) and a
  **12.5x throughput gap** between execution paths of the same procedure
- Query text was **globally redacted by workspace policy**; built an alternative attribution path
  by joining lineage system tables on statement ID, attributing **84.3% of SELECTs** in the peak
  window to specific accounts and tables
- Applied time-boxed autoscaling → **queued queries 90 → 15**
- Validated an incremental physical-load pattern (`REPLACE WHERE`) against a full-recompute view,
  and proved partition pruning actually engages (**17.0s → 3.5s**), which avoided rewriting
  **31 downstream view branches**

### Regression Safety in Data Changes

- Predicted downstream fan-out **before** a grain change — **291,438 → 6,183,444 rows (21.2x)**,
  which would have broken a live dashboard — and redesigned the rollout so the downstream view is
  fixed in the same deployment, with a fixed ordering constraint documented for handover
- Standardized on **bidirectional `EXCEPT ALL` (zero rows both ways)** to prove row-set identity;
  sum-only comparison misses regressions where rows split. Validated a **1.71M-row** downstream
  view as unaffected
- Separated float accumulation-order artifacts (±0.01 under `round(,2)`, exact under
  `decimal(30,6)`) from genuine defects, preventing false defect reports
- Proved a legacy transformation fix lossless under identical input (md5-matched):
  **17 columns matched on all original rows, zero loss**

### Legacy ETL → Databricks Migration Analysis

- Analyzed an on-premise GUI-based ETL (**45 sequential job steps, 25 transformation scripts,
  15 ad media, 35 output columns**) and specified the target pipeline with
  as-is measurement / defect verdict / to-be proposal side by side
- Root-caused why media rows and conversion rows never joined in the final output, and ran a
  **merge-key simulation (current 0% → 97.2% when two derived columns are excluded)** to justify
  the target key design
- Found latent defects that must not be carried over — including a branch filter whose match string
  had **never existed in the source** (0 hits across 2023 and 2026 samples) and a year-prefix filter
  that silently dropped a full year of records (**derived-column fill rate 52% → 90% after fix**)
- *Scope delivered: requirements analysis and defect verdicts. Code migration was scheduled past
  my contract end and handed over.*

### Tooling & Automation

- Built a **network profiler from scratch** (Python + Chrome DevTools Protocol) after the standard
  Node-based tooling was blocked by endpoint security — endpoint p50/p95, automatic
  polling-interval detection, per-second burst fan-out detection
- Automated recurring pipeline work with 4 agent skills and a CLI toolchain, and **encoded safety
  boundaries in a rulebook rather than convention** — writes restricted to dev catalogs, human
  approval required for production runs / releases / backfills, PII columns off-limits

### Core Focus Areas

- Spark execution-plan analysis and executor-level profiling
- Delta Lake data layout (partitioning, liquid clustering, file compaction, transaction log)
- Regression-safe data changes via row-set equivalence proofs
- Multi-tenant query load attribution under restricted observability

---

## Mirae Asset Life Insurance — IT Operations & Data Engineer  
**Feb 2025 – June 2026** <!-- 종료월 확인 후 수정 -->

### Enterprise Data Architecture & BI Engineering

- Design and maintain enterprise **data marts and DW pipelines**
- Develop and optimize **batch ETL workflows** for insurance and financial datasets
- Provide executive-level BI dashboards for C-level decision-making
- Ensure **data integrity, performance optimization, and governance compliance**
- Troubleshoot and optimize production batch jobs and database workloads
- Operated **LLM serving environments on Kubernetes-based model serving infrastructure**

### Core Focus Areas

- Large-scale relational data modeling
- Analytical query performance tuning
- Secure data masking and access control
- Production-grade pipeline reliability

---

# 🚀 Featured Project: Clinical Search Data Pipeline

**Lambda Architecture | Kafka → Spark → S3 → PostgreSQL**

Repository:  
https://github.com/SangjunRyu/clinical-search-data-pipeline

---

## Overview

Designed and implemented an **end-to-end Lambda Architecture data pipeline** processing over **5.2M clinical search log events** (TripClick dataset).

The system combines:

- 📦 **Batch layer** for daily, consistent analytics (T+1)
- ⚡ **Speed layer** for near real-time dashboards (5-minute micro-batch)
- ♻️ **Immutable raw storage** for replay and reprocessing
- 🐳 Fully containerized distributed infrastructure (Docker-based)

This project simulates a production-style hybrid architecture used in real-world data platforms.


## High-Level Architecture

### Ingestion
Web Servers → Kafka (Event Streaming)

### Batch Layer (Accuracy)
Kafka → S3 (Archive Raw) → Spark ETL → PostgreSQL (Batch Marts)

### Speed Layer (Low Latency)
Kafka → Spark Structured Streaming → PostgreSQL (Realtime Marts)

### Serving
PostgreSQL → Apache Superset Dashboards

### Orchestration
Apache Airflow (Pipeline Automation & Scheduling)

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
Databricks (PySpark, Delta Lake, Unity Catalog)  
Apache Airflow  
ETL Pipeline Design  
Data Modeling  
Event-Driven Architecture  

## Performance & Observability
Spark execution plans (`explain codegen`) & executor-level profiling  
Delta Lake layout tuning (partitioning, liquid clustering, compaction)  
Query load attribution via system/lineage tables  
Prometheus, Grafana  

## Cloud & DevOps
AWS (EC2, S3, Lambda, Glue, IAM, VPC)  
Docker  
Kubernetes  
CI/CD  

## Databases
Oracle  
PostgreSQL  
MySQL  
DynamoDB  

## BI
Apache Superset  
Tableau  

---

# 🎓 Education

Bachelor of Engineering  
Computer Science & Electronic Engineering  
Chung-Ang University, Seoul  
GPA: 4.21 / 4.5

- **TOEFL**: 89 (June 2023)
- **Exchange Program**: University of Turku, Finland (Dec 2023 – June 2024)  
  - Participated in software development.

---

# 🌍 Career Objective

Seeking opportunities in:

- Global Tech Companies
- Cloud-native Data Engineering roles
- Distributed Systems & Streaming Infrastructure teams
- ML / AI Infrastructure (inference optimization, model serving, GPU workloads)

I aim to build scalable, fault-tolerant, and intelligent data systems at global scale.
