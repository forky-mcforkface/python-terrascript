# terrascript/nomad/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class nomad_acl_policy(terrascript.Resource):
    pass


class nomad_acl_token(terrascript.Resource):
    pass


class nomad_job(terrascript.Resource):
    pass


class nomad_namespace(terrascript.Resource):
    pass


class nomad_quota_specification(terrascript.Resource):
    pass


class nomad_scheduler_config(terrascript.Resource):
    pass


class nomad_sentinel_policy(terrascript.Resource):
    pass


class nomad_volume(terrascript.Resource):
    pass
