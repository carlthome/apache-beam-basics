"""Windowing Basics (Fixed Windows)"""

import apache_beam as beam
import apache_beam.transforms.window as window
from apache_beam import TimestampedValue

with beam.Pipeline() as p:
    data = p | beam.Create(
        [TimestampedValue("a", 0), TimestampedValue("b", 5), TimestampedValue("c", 15)]
    )

    (
        data
        | beam.WindowInto(window.FixedWindows(10))
        | beam.Map(lambda x: (x, 1))
        | beam.CombinePerKey(sum)
        | beam.Map(print)
    )
