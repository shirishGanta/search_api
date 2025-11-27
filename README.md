\# FastAPI Search API



A simple search API built with FastAPI.  

It provides a `/search` endpoint that returns messages matching a query string.



\## Run Locally

1\. Clone the repo 



\## Bonus 1: Design Notes



While building this search API, I considered a few different design approaches:



1\. \*\*In‑Memory Search (Chosen Approach)\*\*  

&nbsp;  - Store all data in a Python list or dictionary.  

&nbsp;  - Perform simple substring matching using Python’s built‑in functions.  

&nbsp;  - Fast for small datasets and easy to deploy.  

&nbsp;  - Ideal for demo or prototype environments.



2\. \*\*SQLite with Full‑Text Search (FTS5)\*\*  

&nbsp;  - Store data in a lightweight local database.  

&nbsp;  - Use FTS5 indexing for faster text queries.  

&nbsp;  - Scales better for thousands of records while remaining simple to host.



3\. \*\*Elasticsearch / OpenSearch\*\*  

&nbsp;  - Distributed search engine for large‑scale data.  

&nbsp;  - Provides advanced ranking, fuzzy search, and near‑real‑time indexing.  

&nbsp;  - Best for production workloads with millions of records.



I chose the in‑memory approach for simplicity and speed of setup, since the dataset is small and the goal is to demonstrate search and pagination logic.







\## Bonus 2: Data Insights



To reduce latency to around \*\*30 ms\*\*, the following optimizations can be applied:



\- \*\*Keep data in memory:\*\*  

&nbsp; Avoid reading from disk for every request by caching data in memory.



\- \*\*Use asynchronous I/O:\*\*  

&nbsp; Convert endpoints to `async def` and use non‑blocking I/O operations.



\- \*\*Add caching:\*\*  

&nbsp; Use Redis or an in‑memory LRU cache to store frequent query results.



\- \*\*Optimize deployment region:\*\*  

&nbsp; Deploy the API closer to the target users to minimize network latency.



\- \*\*Pre‑index data:\*\*  

&nbsp; Use SQLite FTS5 or Elasticsearch for indexed text search to improve query speed.





