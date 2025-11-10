# Databricks PySpark Notebook - Patient Admissions ETL
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

# Step 1: Setup Spark
spark = SparkSession.builder.appName('PatientAdmissionsETL').getOrCreate()

# Step 2: Load Data
raw_df = spark.read.csv('azure_blob/patient_admissions.csv', header=True)

# Step 3: Data Cleaning
clean_df = raw_df.dropna(subset=['PatientID', 'AdmissionDate'])
clean_df = clean_df.withColumn('AdmissionDate', to_date(col('AdmissionDate'), 'yyyy-MM-dd'))

# Step 4: Transformation
agg_df = clean_df.groupBy('DiagnosisCode').count()
agg_df = agg_df.withColumnRenamed('count', 'AdmissionsCount')

# Step 5: Write to Warehouse
agg_df.write.format('jdbc').option('url', 'jdbc:sqlserver://{your_db}').option('dbtable', 'AdmissionsAgg').save()

# Comments: Each step is modular; edit paths and DB settings as needed for your Azure setup.