# terrascript/newrelic/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class newrelic_alert_channel(terrascript.Resource):
    pass


class newrelic_alert_condition(terrascript.Resource):
    pass


class newrelic_alert_muting_rule(terrascript.Resource):
    pass


class newrelic_alert_policy(terrascript.Resource):
    pass


class newrelic_alert_policy_channel(terrascript.Resource):
    pass


class newrelic_api_access_key(terrascript.Resource):
    pass


class newrelic_application_settings(terrascript.Resource):
    pass


class newrelic_dashboard(terrascript.Resource):
    pass


class newrelic_entity_tags(terrascript.Resource):
    pass


class newrelic_events_to_metrics_rule(terrascript.Resource):
    pass


class newrelic_infra_alert_condition(terrascript.Resource):
    pass


class newrelic_insights_event(terrascript.Resource):
    pass


class newrelic_nrql_alert_condition(terrascript.Resource):
    pass


class newrelic_one_dashboard(terrascript.Resource):
    pass


class newrelic_plugins_alert_condition(terrascript.Resource):
    pass


class newrelic_synthetics_alert_condition(terrascript.Resource):
    pass


class newrelic_synthetics_monitor(terrascript.Resource):
    pass


class newrelic_synthetics_monitor_script(terrascript.Resource):
    pass


class newrelic_synthetics_multilocation_alert_condition(terrascript.Resource):
    pass


class newrelic_synthetics_secure_credential(terrascript.Resource):
    pass


class newrelic_workload(terrascript.Resource):
    pass
