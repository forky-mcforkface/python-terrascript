# terrascript/dns/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class dns_a_record_set(terrascript.Data):
    pass


class dns_aaaa_record_set(terrascript.Data):
    pass


class dns_cname_record_set(terrascript.Data):
    pass


class dns_mx_record_set(terrascript.Data):
    pass


class dns_ns_record_set(terrascript.Data):
    pass


class dns_ptr_record_set(terrascript.Data):
    pass


class dns_srv_record_set(terrascript.Data):
    pass


class dns_txt_record_set(terrascript.Data):
    pass
