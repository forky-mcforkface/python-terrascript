# terrascript/random/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class random_id(terrascript.Resource):
    pass


class random_integer(terrascript.Resource):
    pass


class random_password(terrascript.Resource):
    pass


class random_pet(terrascript.Resource):
    pass


class random_shuffle(terrascript.Resource):
    pass


class random_string(terrascript.Resource):
    pass


class random_uuid(terrascript.Resource):
    pass
