# terrascript/heroku/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class heroku_addon(terrascript.Data):
    pass


class heroku_app(terrascript.Data):
    pass


class heroku_pipeline(terrascript.Data):
    pass


class heroku_space(terrascript.Data):
    pass


class heroku_space_peering_info(terrascript.Data):
    pass


class heroku_team(terrascript.Data):
    pass
