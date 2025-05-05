"""Grouping and Reductions"""

import apache_beam as beam

with beam.Pipeline() as p:
    nums = p | beam.Create([1, 2, 3, 4, 5, 6])

    # Global sum
    nums | "Global sum" >> beam.CombineGlobally(sum) | beam.Map(print)

    # GroupByKey example
    kvs = p | beam.Create([("a", 1), ("a", 2), ("b", 3)])
    grouped = kvs | beam.GroupByKey()
    grouped | beam.Map(print)
