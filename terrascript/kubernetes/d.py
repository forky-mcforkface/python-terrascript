# terrascript/kubernetes/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class kubernetes_all_namespaces(terrascript.Data):
    pass


class kubernetes_config_map(terrascript.Data):
    pass


class kubernetes_ingress(terrascript.Data):
    pass


class kubernetes_namespace(terrascript.Data):
    pass


class kubernetes_persistent_volume_claim(terrascript.Data):
    pass


class kubernetes_pod(terrascript.Data):
    pass


class kubernetes_secret(terrascript.Data):
    pass


class kubernetes_service(terrascript.Data):
    pass


class kubernetes_service_account(terrascript.Data):
    pass


class kubernetes_storage_class(terrascript.Data):
    pass
