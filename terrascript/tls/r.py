# terrascript/tls/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class tls_cert_request(terrascript.Resource):
    pass


class tls_locally_signed_cert(terrascript.Resource):
    pass


class tls_private_key(terrascript.Resource):
    pass


class tls_self_signed_cert(terrascript.Resource):
    pass
