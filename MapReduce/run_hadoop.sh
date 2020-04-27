hdfs dfs -rm -r output
hadoop jar /hadoop-3.1.3/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input $1 -output output
