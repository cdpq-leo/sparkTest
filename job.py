import pyspark

conf = pyspark.SparkConf()
conf.setMaster("mesos://leader.mesos:5050")
conf.setAppName("Test Alluxio")
conf.set("spark.mesos.executor.docker.image", "cdpqleo/spark:2.3.1-2.2.1-2-hadoop-2.6")
conf.set("spark.mesos.executor.home", "/opt/spark/dist")
conf.set("spark.mesos.coarse", "true")
conf.set("spark.driver.memory", "512m")
conf.set("spark.executor.memory", "512m")
conf.set("spark.executor.cores", "1")
conf.set("spark.eventLog.enabled", "false")
conf.set("spark.submit.deployMode", "client")

sc = pyspark.SparkContext(conf=conf)

file = sc.textFile("hdfs://hdfs/user/jsaba/College.csv")
print file.count()
