# terrascript/signalfx/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class signalfx_aws_services(terrascript.Data):
    pass


class signalfx_azure_services(terrascript.Data):
    pass


class signalfx_dimension_values(terrascript.Data):
    pass


class signalfx_gcp_services(terrascript.Data):
    pass


class signalfx_pagerduty_integration(terrascript.Data):
    pass
