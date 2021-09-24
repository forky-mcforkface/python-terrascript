# tests/test_provider_kvrhdn_honeycombio.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:18:50 UTC)


def test_provider_import():
    import terrascript.provider.kvrhdn.honeycombio


def test_resource_import():
    from terrascript.resource.kvrhdn.honeycombio import honeycombio_board

    from terrascript.resource.kvrhdn.honeycombio import honeycombio_column

    from terrascript.resource.kvrhdn.honeycombio import honeycombio_dataset

    from terrascript.resource.kvrhdn.honeycombio import honeycombio_derived_column

    from terrascript.resource.kvrhdn.honeycombio import honeycombio_marker

    from terrascript.resource.kvrhdn.honeycombio import honeycombio_trigger


def test_datasource_import():
    from terrascript.data.kvrhdn.honeycombio import honeycombio_datasets

    from terrascript.data.kvrhdn.honeycombio import honeycombio_query

    from terrascript.data.kvrhdn.honeycombio import honeycombio_trigger_recipient


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.kvrhdn.honeycombio
#
#      t = terrascript.provider.kvrhdn.honeycombio.honeycombio()
#      s = str(t)
#
#      assert 'https://github.com/kvrhdn/terraform-provider-honeycombio' in s
#      assert '0.1.4' in s
