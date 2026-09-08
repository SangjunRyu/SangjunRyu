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

Worked across the **analytics-facing layer** of a multi-account advertising data platform
(Databricks · PySpark · Delta Lake · Unity Catalog) — gold datasets, ODBC report views, and
Tableau dashboards consumed by marketing teams — plus the performance and reliability engineering
underneath them. Ingestion through the silver layer was owned by a separate platform cell.

- Optimized the URL classification stage of a **24.5M-row Spark batch** using `explain codegen`
  and measured traffic distribution to reorder branch conditions and short-circuit regex
  evaluation — including **executor-level UDF profiling that disproved my initial
  regex-bottleneck hypothesis**. Verified row-set equivalence before release;
  **shipped to production**
- Attributed peak-hour query load on a shared SQL warehouse to account and table level using
  **Databricks system / lineage tables** when query text was globally redacted by policy
  (**84.3%** of SELECTs attributed), then applied time-boxed autoscaling —
  **queued queries 90 → 15**
- Analyzed a legacy on-premise ETL (**45 sequential steps · 15 ad media · 35 output columns**)
  for Databricks migration — measured AS-IS behavior on real data, issued defect verdicts, and
  designed the target data model and merge keys via **key-combination simulation (0% → 97.2%)**
- Translated campaign-analytics requirements from marketing teams into **dataset specs** —
  metric definitions, grain, key uniqueness, partitioning, and how far back data could be
  restated — and delivered them as gold datasets, report views, and dashboards

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

Currently focused on data platform and ML/AI infrastructure — inference optimization,
model serving, and GPU workloads.
