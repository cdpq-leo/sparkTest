import pyspark
import datetime

conf = pyspark.SparkConf()
conf.setMaster("mesos://leader.mesos:5050")
conf.setAppName("Test locality")
conf.set("spark.mesos.executor.docker.image", "cdpqleo/spark:2.3.1-2.2.1-2-hadoop-2.6-alluxio")
conf.set("spark.mesos.executor.home", "/opt/spark/dist")
conf.set("spark.mesos.coarse", "true")
conf.set("spark.driver.memory", "512m")
conf.set("spark.executor.memory", "2g")
conf.set("spark.executor.cores", "1")
conf.set("spark.submit.deployMode", "client")
conf.set("spark.executor.instances", "3")
conf.set("spark.cores.max", "1")
conf.set("spark.eventLog.enabled", "true")
conf.set("spark.eventLog.dir", "hdfs://hdfs/app/spark/2.3.0/logs")
conf.set("spark.mesos.executor.docker.volumes", "/mnt/ramdisk:/opt/ramdisk")

sc = pyspark.SparkContext(conf=conf)
sc._jsc.hadoopConfiguration.set("fs.DefaultFS", "alluxio://alluxio-master.alluxio.marathon.mesos:19998")

file = sc.textFile("hdfs://hdfs/user/lpbonenfant/sample2.csv")
file.saveAsTextFile("alluxio://alluxio-master.alluxio.marathon.mesos:19998:/user/lpbonenfant/sample3.csv")
file1 = sc.textFile("alluxio://alluxio-master.alluxio.marathon.mesos:19998:/user/lpbonenfant/sample3.csv")
file1.filter(lambda x: "Spark" in x[1]).count()

before = datetime.datetime.now()
for i in range(0,40):
    file1.filter(lambda x: "Spark" in x[1]).count()
after = datetime.datetime.now()
d = after - before
print d.total_seconds()
