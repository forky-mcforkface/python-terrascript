# terrascript/tls/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class tls_certificate(terrascript.Data):
    pass


class tls_public_key(terrascript.Data):
    pass
