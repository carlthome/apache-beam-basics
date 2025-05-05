"""Example: Total duration of music track — Mapping & Reducing"""

import apache_beam as beam

tracks = [
    {"title": "Song A", "genre": "pop", "duration": 210},
    {"title": "Song B", "genre": "rock", "duration": 180},
    {"title": "Song C", "genre": "pop", "duration": 200},
    {"title": "Song D", "genre": "jazz", "duration": 240},
]

with beam.Pipeline() as p:
    (
        p
        | "Create tracks" >> beam.Create(tracks)
        # Map to (genre, duration)
        | "Extract genre & duration"
        >> beam.Map(lambda track: (track["genre"], track["duration"]))
        # Sum durations per genre
        | "Total duration per genre" >> beam.CombinePerKey(sum)
        | "Print results" >> beam.Map(print)
    )
