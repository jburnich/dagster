from dagster._core.libraries import DagsterLibraryRegistry

from .resources import DataDogClientResource, datadog_resource
from .version import __version__

DagsterLibraryRegistry.register("dagster-datadog", __version__)

__all__ = ["datadog_resource", "DataDogClientResource"]
