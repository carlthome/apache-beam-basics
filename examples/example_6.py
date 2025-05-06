"""Windowing basics"""

import apache_beam as beam
from apache_beam.transforms.window import FixedWindows, TimestampedValue

with beam.Pipeline() as p:
    collection = p | beam.Create(
        [
            TimestampedValue("a", 0),
            TimestampedValue("b", 5),
            TimestampedValue("b", 7),
            TimestampedValue("c", 15),
            TimestampedValue("c", 30),
            TimestampedValue("c", 35),
            TimestampedValue("c", 37),
        ]
    )

    (
        collection
        | beam.WindowInto(FixedWindows(10))
        | beam.Map(lambda x: (x, 1))
        | beam.CombinePerKey(sum)
        | beam.Map(print)
    )
