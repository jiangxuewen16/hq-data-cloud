from pyspark import SparkContext

sc = SparkContext("local", "First App")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"
     ])
counts = words.filter(lambda x: 'spark' in x).collect()
print(counts)