// Author: Christopher Lawrie from CERN
// https://db-blog.web.cern.ch/blog/christopher-lawrie/2016-08-experiences-using-alluxio-spark

def time[R](block: => R): R = {                                     // Function to time actions.
    val t0 = System.nanoTime()
    val result = block    // call-by-name
    val t1 = System.nanoTime()
    println("Elapsed time: " + (t1 - t0) + "ns")
    result
 }

val file = sc.textFile("hdfs://hdfs/user/lpbonenfant/sample.csv")   // Reference file from HDFS.
 file.cache                                                         // Set it to be cached in memory.
 file.filter(line => line.contains("BALTIMORE")).collect            // Cache file.

time( for ( a <- 1 to 40) {                                         // Run filter 40 times on cached file.
       file.filter(line => line.contains("BALTIMORE")).collect
    }
 )
