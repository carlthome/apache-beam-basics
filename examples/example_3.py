"""Grouping and reduce transformations"""

import apache_beam as beam

with beam.Pipeline() as p:
    # Global sum
    collection1 = p | "Data" >> beam.Create([1, 2, 3, 4, 5, 6])
    total = collection1 | beam.CombineGlobally(sum)
    total | "Show sum" >> beam.Map(print)

    # GroupByKey example
    collection2 = p | "Keyed data" >> beam.Create([("a", 1), ("a", 2), ("b", 3)])
    groups = collection2 | beam.GroupByKey()
    groups | "Show groups" >> beam.Map(print)
