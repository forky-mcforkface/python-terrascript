# terrascript/scaleway/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class scaleway_account_ssh_key(terrascript.Data):
    pass


class scaleway_baremetal_offer(terrascript.Data):
    pass


class scaleway_instance_image(terrascript.Data):
    pass


class scaleway_instance_security_group(terrascript.Data):
    pass


class scaleway_instance_server(terrascript.Data):
    pass


class scaleway_instance_volume(terrascript.Data):
    pass


class scaleway_k8s_cluster(terrascript.Data):
    pass


class scaleway_k8s_pool(terrascript.Data):
    pass


class scaleway_lb_ip(terrascript.Data):
    pass


class scaleway_marketplace_image(terrascript.Data):
    pass


class scaleway_rdb_instance(terrascript.Data):
    pass


class scaleway_registry_image(terrascript.Data):
    pass


class scaleway_registry_namespace(terrascript.Data):
    pass


class scaleway_vpc_private_network(terrascript.Data):
    pass
