"""ParDo for More Control"""

import apache_beam as beam


class MultiplyByTwo(beam.DoFn):
    def process(self, element):
        yield element * 2


with beam.Pipeline() as p:
    p | beam.Create([1, 2, 3]) | beam.ParDo(MultiplyByTwo()) | beam.Map(print)
