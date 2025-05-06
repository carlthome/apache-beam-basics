"""Basic transformations in Apache Beam."""

import apache_beam as beam

data = [1, 2, 3]

a = data | beam.Map(lambda x: print(x + 2))

b = data | beam.Map(lambda x: x + 2) | beam.LogElements()
