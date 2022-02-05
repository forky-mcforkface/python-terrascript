# tests/test_provider_circonus-labs_circonus.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:13:59 UTC)


def test_provider_import():
    import terrascript.provider.circonus_labs.circonus


def test_resource_import():
    from terrascript.resource.circonus_labs.circonus import circonus_check

    from terrascript.resource.circonus_labs.circonus import circonus_contact_group

    from terrascript.resource.circonus_labs.circonus import circonus_dashboard

    from terrascript.resource.circonus_labs.circonus import circonus_graph

    from terrascript.resource.circonus_labs.circonus import circonus_maintenance

    from terrascript.resource.circonus_labs.circonus import circonus_metric

    from terrascript.resource.circonus_labs.circonus import circonus_overlay_set

    from terrascript.resource.circonus_labs.circonus import circonus_rule_set

    from terrascript.resource.circonus_labs.circonus import circonus_rule_set_group

    from terrascript.resource.circonus_labs.circonus import circonus_worksheet


def test_datasource_import():
    from terrascript.data.circonus_labs.circonus import circonus_account

    from terrascript.data.circonus_labs.circonus import circonus_collector


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.circonus_labs.circonus
#
#      t = terrascript.provider.circonus_labs.circonus.circonus()
#      s = str(t)
#
#      assert 'https://github.com/circonus-labs/terraform-provider-circonus' in s
#      assert '0.12.2' in s