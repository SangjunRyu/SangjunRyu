# Sangjun You

**Data Engineer | Data Platform | Systems & Performance Engineering**

Data Engineer with ~1.5 years of enterprise DW/BI experience (Oracle · Hadoop · DataStage) followed by
hands-on work on a modern **Databricks / Spark / Delta Lake** platform. I like problems where the fix
comes from reading the execution plan and the profiler rather than guessing — pipeline performance,
data layout, and proving a change didn't break anything.

📌 LinkedIn — https://www.linkedin.com/in/sangjun-you-a29442257/

---

# 💼 Selected Experience

## Mirae Asset Life Insurance — Data Engineer, IT Operations
**Feb 2025 – Jun 2026**

Enterprise DW and analytics operations for insurance and financial datasets.

<!-- ⚠️ 아래 4개 수치(44% / 1주→1일 / 480GB→31GB / 500GB)는 확인 후 확정할 것 -->

- Operated **ETL and data marts across Oracle DW and Hadoop** environments using
  DataStage, Hive, and Spark
- Improved scoring pipeline lead time by **44%** through batch partitioning and
  removal of inefficient library calls
- Automated a KPI reporting workflow from **~1 week to ~1 day** turnaround
- Restructured `SQL*Loader` ingestion to cut intermediate storage from **~480GB to ~31GB**,
  reclaiming **~500GB** of database space
- Supported **enterprise BI and financial reporting** on Tableau and Cognos for
  executive-level decision-making
- Supported **container and GPU deployment / troubleshooting for AI inference workloads
  on Kubernetes**-based model serving infrastructure
- Applied data masking and access controls for governance compliance

---

## Echo Marketing — Data Engineer (Contract)
**Jun 2026 – Sep 2026**

Developed and maintained **gold-layer pipelines and BI serving workloads** on a multi-account
advertising data platform (Databricks · PySpark · Delta Lake · Unity Catalog). Ingestion through
the silver layer was owned by a separate platform cell.

- Optimized the URL classification stage of a **24.5M-row Spark batch** using `explain codegen`
  and measured traffic distribution to reorder branch conditions and short-circuit regex
  evaluation — including **executor-level UDF profiling that disproved my initial
  regex-bottleneck hypothesis**. Verified row-set equivalence before release;
  **shipped to production**
- Attributed peak-hour query load on a shared SQL warehouse to account and table level using
  **Databricks system / lineage tables** when query text was globally redacted by policy
  (**84.3%** of SELECTs attributed), then applied time-boxed autoscaling —
  **queued queries 90 → 15**
- Managed regression risk in data changes — predicted downstream fan-out **before** a grain change
  (**21.2x** row inflation that would have broken a live dashboard) and standardized on
  **bidirectional row-set equivalence checks** instead of aggregate comparison
- Analyzed a legacy on-premise ETL (**45 sequential steps · 15 ad media · 35 output columns**)
  for Databricks migration — measured AS-IS behavior on real data, issued defect verdicts, and
  designed the target data model and merge keys via **key-combination simulation (0% → 97.2%)**
- Built a **network profiling utility** (Python + Chrome DevTools Protocol) after Node-based
  tooling was blocked by endpoint security — endpoint p50/p95, polling-interval detection,
  burst fan-out detection

---

# 🚀 Featured Engineering Projects

## Clinical Search Data Pipeline — Lambda Architecture

**Kafka → Spark → S3 → PostgreSQL → Superset · orchestrated with Airflow**

https://github.com/SangjunRyu/clinical-search-data-pipeline

End-to-end Lambda Architecture pipeline processing **5.2M+ clinical search log events**
(TripClick dataset), fully containerized with Docker.

- **Batch layer** — Kafka → S3 (immutable raw archive) → Spark ETL → PostgreSQL marts (T+1)
- **Speed layer** — Kafka → Spark Structured Streaming → PostgreSQL realtime marts (5-min micro-batch)
- **Replay** — raw archive retained for reprocessing
- **Serving** — Apache Superset dashboards

## AWS 3-Tier Architecture

https://github.com/SangjunRyu/AWS-3tier-Architecture

Scalable 3-tier design — EC2 + load balancer, Apache reverse proxy, Prometheus/Grafana monitoring,
S3 log archiving. Validated under concurrent simulated traffic with K6.

## Fire Emergency Response Data Platform

https://github.com/SangjunRyu/Cloud9-Final-Project

Batch and real-time analytics on emergency response times — AWS Glue ETL, Lambda streaming
ingestion, SNS alerting. Analysis targeted the 7-minute golden-time objective.

---

# 🛠 Technical Stack

**Languages** — Python, Java, SQL, C++

**Data** — Spark (batch & streaming), Databricks (PySpark · Delta Lake · Unity Catalog), Kafka,
Airflow, DataStage, Hive, ETL & data modeling

**Performance & Observability** — Spark execution plans (`explain codegen`), executor-level
profiling, Delta layout tuning (partitioning · clustering · compaction), query load attribution
via system/lineage tables, Prometheus, Grafana

**Cloud & DevOps** — AWS (EC2, S3, Lambda, Glue, IAM, VPC), Docker, Kubernetes, CI/CD

**Databases** — Oracle, PostgreSQL, MySQL, DynamoDB

**BI** — Tableau, Cognos, Superset

---

# 🎓 Education

**Bachelor of Engineering**, Computer Science & Electronic Engineering
Chung-Ang University, Seoul — GPA 4.21 / 4.5

- Exchange program — University of Turku, Finland (Dec 2023 – Jun 2024)
- TOEFL 89 (Jun 2023)

---

# 🌍 Career Objective

Seeking opportunities in:

- Global Tech Companies
- Cloud-native Data Engineering roles
- Distributed Systems & Streaming Infrastructure teams
- ML / AI Infrastructure (inference optimization, model serving, GPU workloads)

I aim to build scalable, fault-tolerant, and intelligent data systems at global scale.
