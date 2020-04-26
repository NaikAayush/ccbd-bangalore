hdfs dfs -rm -r output
hadoop jar /hadoop-3.1.3/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar -file mapper.py -mapper mapper.py -file reducer_rollingavg.py -reducer reducer_rollingavg.py -input main.csv -output output
