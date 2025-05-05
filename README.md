# Apache Beam basics

A short crash course in authoring Beam pipelines using Python.

## Get started

### Prerequisites

Make sure you have a recent Python version installed on your machine.

### Install

```sh
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel

# Install Apache Beam
pip install apache-beam
```

### Run examples

Each example is a standalone Python script that demonstrates a specific feature of the Apache Beam domain-specific language (DSL). You can run each example by executing the following command in your terminal:

```sh
python examples/example_1.py
```

## FAQ

### What about production?

In a production environment, you would typically author Beam pipelines using the Apache Beam SDK and run them on a distributed processing engine such as Google Cloud Dataflow.

Some gotchas to be aware of:

- It's good to author pipelines such as all elements are about the same byte size. This is because the data is serialized and sent around. If you have a large element, it can cause performance issues or even crashes (disk, memory, etc.).
- Normally the pipeline input is not a regular Python list, but rather a PCollection that is only materialized when the pipeline is run (e.g. `beam.io.ReadFromText` and `beam.io.ReadFromBigQuery`).
- Your functions have to be seralizable to be sent to additional workers. A good test is to run `pickle.loads(pickle.dumps(your_function))`.
- Dependencies have to be available on the workers.
- Configuring hardware resources (e.g. machine types, number of processes and threads, etc.) is surprisingly challenging.
