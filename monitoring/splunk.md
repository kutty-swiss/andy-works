# About Splunk

**Splunk** is a powerful platform used for searching, monitoring, and analyzing machine-generated data in real time. In my case, I use **Splunk** for a variety of purposes including **incident analysis**, **assessing impacted user journeys**, tracking **user counts**, performing **proactive monitoring**, calculating **impact assessments**, and generating **reports**.

On a regular basis, I use **Splunk** for these tasks and have consolidated **Splunk queries** and **Splunk dashboards** on separate pages, organized by the specific applications I work with. Since installing **Splunk** locally is typically not feasible, I have documented the most important queries and variations that have proven useful in my work.

---

## How Splunk Queries Work

Splunk queries generally serve two main purposes:

1. **Filtering and Fetching Data**: Narrowing down large datasets based on specific criteria.
2. **Formatting and Presenting Data**: Formatting the fetched data in a way that is easy to understand, analyze, and visualize.

### Tips for Filtering Data

- **Start with shorter time ranges** and then expand if needed. This helps reduce the data load and speeds up the query.
- **Know your indexes**: Always check which indexes contain the relevant data to optimize search performance.
- **Leverage the `sourcetype` field**: Use this to refine searches based on the specific data types.
- **Use verbose mode sparingly**: Enabling verbose mode provides detailed logs, which can slow down searches. Only enable it when necessary.
- **Make use of `where` clauses and sub-searches**: These are useful for more precise filtering.

### Tips for Formatting Data

To present data in a more readable and actionable way, Splunk provides several powerful commands:

- **rex**: Extract fields using regular expressions.
- **stats**: Perform aggregations like sum, count, average, etc.
- **timechart**: Generate time-based visualizations for trends over time.
- **head**: Limit the results to the first N rows.
- **sort**: Sort results in ascending or descending order.
- **spath**: Extract structured data from fields like JSON or XML.
- **eval**: Create new fields or modify existing ones.
- **replace**: Substitute values in fields.
- **rename**: Rename fields for better clarity.
- **table**: Display the results in a tabular format.

Additionally, I utilize **custom field extraction** and reference **CSV lookup tables** for enriching the queries and improving data quality.

---

## Commonly Used Splunk Clauses and Examples

### **`search`** Clause

The `search` clause is the foundation of any query in Splunk. It allows you to filter and retrieve specific data from indexed sources.

Example:
```spl
index=web_logs sourcetype=access_combined status=200


This query counts the number of occurrences of each status code in the web logs.

```spl
index=web_logs sourcetype=access_combined
| stats count by status
```

This query counts the number of occurrences of each status code in the web logs.

### **`timechart`** Clause

The `timechart` clause is used to generate time-based visualizations, particularly useful for analyzing time-series data.

Example:
```spl
index=web_logs sourcetype=access_combined
| timechart span=1h count by status
```

This query generates a timechart, grouping data by hour (`span=1h`) and counting occurrences for each status code.

### **`rex`** Clause

The `rex` clause allows for regular expression field extraction, ideal when dealing with unstructured data.

Example:
```spl
index=web_logs sourcetype=access_combined
| rex field=_raw "user_agent=\"(?<user_agent>.*?)\""
| stats count by user_agent
```

This query extracts the user agent from raw logs and counts the occurrences of each user agent.

### **`eval`** Clause

The `eval` clause enables you to create new fields or modify existing ones using expressions.

Example:
```spl
index=web_logs sourcetype=access_combined
| eval error_rate = if(status >= 400, 1, 0)
| stats sum(error_rate) as total_errors
```

This query creates an `error_rate` field based on HTTP status codes (marks 1 for errors and 0 for successes) and calculates the total number of errors.


### **`lookup`** Clause

The `lookup` clause is used to enrich your Splunk data by referencing external CSV files or lookup tables.

Example:
```spl
index=web_logs sourcetype=access_combined
| lookup user_info.csv user_id OUTPUT user_name user_email
| stats count by user_name
```

This query uses a lookup table (`user_info.csv`) to map `user_id` to `user_name` and `user_email`, then counts occurrences by `user_name`.


### **`fields`** Clause

The `fields` clause allows you to include or exclude specific fields in your results, optimizing performance and clarity.

Example:
```spl
index=web_logs sourcetype=access_combined
| fields host, status, bytes
```

This query limits the output to only the `host`, `status`, and `bytes` fields.

### **`dedup`** Clause

The `dedup` clause removes duplicate events based on specified fields, ensuring unique results.

Example:
```spl
index=web_logs sourcetype=access_combined
| dedup session_id
| stats count by session_id
```

This query removes duplicate events for each `session_id` and counts the unique sessions.

### **`top`** Clause

The `top` clause provides a quick way to find the most common values in a field.

Example:
```spl
index=web_logs sourcetype=access_combined
| top user_agent
```

This query lists the most common user agents along with their counts and percentages.

### **`eventstats`** Clause

The `eventstats` clause calculates statistics and appends them to each event without reducing the number of events.

Example:
```spl
index=web_logs sourcetype=access_combined
| eventstats avg(bytes) as avg_bytes
| eval above_avg = if(bytes > avg_bytes, "yes", "no")
```

This query calculates the average bytes across all events, appends it to each event, and flags events with bytes above the average.

## Dashboards

I am a strong user of dashboards in Splunk, mainly because they provide a range of powerful visualization options. However, since Splunk cannot be installed on my local machine, I cannot display dashboard snapshots here. That being said, dashboards are incredibly useful for repeated monitoring of standard data and presenting that data through rich visualizations, making it easier to spot trends and outliers.

Although AppDynamics is faster in terms of performance, Splunk has a distinct edge when it comes to the customization of queries and the flexibility it offers. In terms of creating tailored reports and deeper analysis, Splunk provides a lot more versatility than AppDynamics.