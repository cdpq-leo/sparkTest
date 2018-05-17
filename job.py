import pyspark

conf = pyspark.SparkConf()
conf.setMaster("mesos://leader.mesos:5050")
conf.setAppName("Test locality")
conf.set("spark.mesos.executor.docker.image", "cdpqleo/spark:2.3.1-2.2.1-2-hadoop-2.6-alluxio")
conf.set("spark.mesos.executor.home", "/opt/spark/dist")
conf.set("spark.mesos.coarse", "true")
conf.set("spark.driver.memory", "512m")
conf.set("spark.executor.memory", "2g")
conf.set("spark.executor.cores", "1")
conf.set("spark.eventLog.enabled", "false")
conf.set("spark.submit.deployMode", "client")
conf.set("spark.executor.instances", "1")
conf.set("spark.cores.max", "1")
conf.set("spark.eventLog.enabled", "true")
conf.set("spark.eventLog.dir", "hdfs://hdfs/app/spark/2.3.0/logs")
conf.set("spark.mesos.constraints", "privatenodetype:stateless")


sc = pyspark.SparkContext(conf=conf)

file = sc.textFile("alluxio://alluxio-master.alluxio.marathon.mesos:19998/users/lpbonenfant/sample.csv")
print file.count()
