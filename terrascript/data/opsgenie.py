# terrascript/data/opsgenie.py
import terrascript


class opsgenie_escalation(terrascript.Data):
    pass


class opsgenie_heartbeat(terrascript.Data):
    pass


class opsgenie_schedule(terrascript.Data):
    pass


class opsgenie_service(terrascript.Data):
    pass


class opsgenie_team(terrascript.Data):
    pass


class opsgenie_user(terrascript.Data):
    pass


__all__ = [
    "opsgenie_escalation",
    "opsgenie_heartbeat",
    "opsgenie_schedule",
    "opsgenie_service",
    "opsgenie_team",
    "opsgenie_user",
]
