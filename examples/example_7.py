"""Example: Total duration of music tracks"""

import apache_beam as beam

tracks = [
    {"title": "Song A", "genre": "pop", "duration": 210},
    {"title": "Song B", "genre": "rock", "duration": 180},
    {"title": "Song C", "genre": "pop", "duration": 200},
    {"title": "Song D", "genre": "jazz", "duration": 240},
]


def get_duration(track):
    genre = track["genre"]
    duration = track["duration"]
    return genre, duration


with beam.Pipeline() as p:
    (
        p
        | "Create tracks" >> beam.Create(tracks)
        | "Extract genre and duration" >> beam.Map(get_duration)
        | "Total duration per genre" >> beam.CombinePerKey(sum)
        | "Print results" >> beam.Map(print)
    )
