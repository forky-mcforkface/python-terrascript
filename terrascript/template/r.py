# terrascript/template/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class template_cloudinit_config(terrascript.Resource):
    pass


class template_dir(terrascript.Resource):
    pass


class template_file(terrascript.Resource):
    pass
