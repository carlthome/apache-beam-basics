"""FlatMap & Flatten"""

import apache_beam as beam

with beam.Pipeline() as p:
    # FlatMap: explode
    (
        p
        | beam.Create(["hello world"])
        | beam.FlatMap(lambda x: x.split())
        | beam.Map(print)
    )

    # Flatten: merge multiple PCollections
    a = p | "List A" >> beam.Create([1, 2])
    b = p | "List B" >> beam.Create([3, 4])
    (a, b) | beam.Flatten() | beam.Map(print)
