"""Basic Transformations"""

import apache_beam as beam

with beam.Pipeline() as p:
    # Initial list
    collection = p | beam.Create([1, 2, 3])

    # Map: Add 2
    collection | beam.Map(lambda x: x + 2) | beam.Map(print)

    # Logging side-effect
    collection | beam.Map(lambda x: x + 2) | beam.LogElements()
