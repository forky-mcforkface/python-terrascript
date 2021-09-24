# tests/test_provider_mercari_spinnaker.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:27:28 UTC)


def test_provider_import():
    import terrascript.provider.mercari.spinnaker


def test_resource_import():
    from terrascript.resource.mercari.spinnaker import spinnaker_application

    from terrascript.resource.mercari.spinnaker import spinnaker_canary_config

    from terrascript.resource.mercari.spinnaker import spinnaker_pipeline

    from terrascript.resource.mercari.spinnaker import spinnaker_pipeline_template

    from terrascript.resource.mercari.spinnaker import spinnaker_project


def test_datasource_import():
    from terrascript.data.mercari.spinnaker import spinnaker_application

    from terrascript.data.mercari.spinnaker import spinnaker_canary_config

    from terrascript.data.mercari.spinnaker import spinnaker_pipeline

    from terrascript.data.mercari.spinnaker import spinnaker_project


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.mercari.spinnaker
#
#      t = terrascript.provider.mercari.spinnaker.spinnaker()
#      s = str(t)
#
#      assert 'https://github.com/mercari/terraform-provider-spinnaker' in s
#      assert '0.3.0' in s
