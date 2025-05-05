"""Filtering & Branching"""

import apache_beam as beam

with beam.Pipeline() as p:
    elements = p | beam.Create([1, 2, 3, 4, 5]) | beam.Map(lambda x: x + 2)

    # Log all elements
    elements | "Log all" >> beam.LogElements()

    # Filter even numbers
    elements | beam.Filter(lambda x: x % 2 == 0) | "Log even" >> beam.LogElements()
