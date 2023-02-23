from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
)
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

resource = Resource(attributes={
    SERVICE_NAME: "your-service-name"
})
aspectoToken = "your-aspecto-token"
headers = f"Authorization={aspectoToken}"

provider = TracerProvider(resource=resource)
aspecto_exporter = OTLPSpanExporter(endpoint="https://otelcol.aspecto.io:4317", headers=headers)
processor = BatchSpanProcessor(aspecto_exporter)
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

print('opentelemetry is setup')
