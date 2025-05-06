"""Filtering and branching"""

import apache_beam as beam

with beam.Pipeline() as p:
    collection = p | beam.Create([1, 2, 3, 4, 5]) | beam.Map(lambda x: x + 2)

    # Log all elements
    collection | "Log all" >> beam.LogElements()

    # Filter even numbers
    evens = (
        collection
        | beam.Filter(lambda x: x % 2 == 0)
        | "Log even" >> beam.LogElements()
    )
