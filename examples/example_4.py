"""ParDo for custom processing."""

import apache_beam as beam


class Multiply(beam.DoFn):
    def __init__(self, factor: int):
        super().__init__()
        self.factor = factor

    def process(self, element):
        yield element * self.factor


with beam.Pipeline() as p:
    p | beam.Create([1, 2, 3]) | beam.ParDo(Multiply(2)) | beam.Map(print)
