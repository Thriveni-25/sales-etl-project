# Incremental Load ETL Pipeline using Azure Data Factory

## Overview

Developed an Incremental Load ETL Pipeline using Azure Data Factory and Azure SQL Database. The pipeline uses a watermark table approach to identify and load only newly arrived records, reducing duplicate processing and improving ETL efficiency.

## Technologies Used

* Azure Data Factory (ADF)
* Azure SQL Database
* SQL
* Azure Blob Storage

## Architecture

CSV File → Azure Blob Storage → Azure Data Factory → Azure SQL Database

## Workflow

1. Read the last processed ORDERNUMBER from the watermark table.
2. Retrieve the watermark value using a Lookup Activity.
3. Load only new records into the target table.
4. Update the watermark table with the latest ORDERNUMBER.
5. Validate the loaded records using SQL queries.

## Database Objects

### Target Table

* sales_incremental

### Watermark Table

* watermark_table

## ADF Components

* Lookup Activity
* Copy Data Activity
* Azure SQL Dataset
* Azure Blob Storage Dataset

## SQL Query Used in Lookup Activity

```sql
SELECT last_order_number
FROM watermark_table;
```

## Dynamic Expression Used

```text
@activity('GetWatermark').output.firstRow.last_order_number
```

## Key Concepts Demonstrated

* Incremental Load
* ETL Pipeline Development
* Watermark Table Logic
* Azure Data Factory
* Azure SQL Database
* Data Validation
* Lookup Activity

## Outcome

Successfully implemented an Incremental Load process that loads only new records into Azure SQL Database and updates the watermark value after each successful execution.
