# tests/test_provider_PortOfPortland_activedirectory.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:10:54 UTC)


def test_provider_import():
    import terrascript.provider.PortOfPortland.activedirectory


def test_resource_import():
    from terrascript.resource.PortOfPortland.activedirectory import (
        activedirectory_groupMembership,
    )

    from terrascript.resource.PortOfPortland.activedirectory import (
        activedirectory_ouMapping,
    )


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.PortOfPortland.activedirectory
#
#      t = terrascript.provider.PortOfPortland.activedirectory.activedirectory()
#      s = str(t)
#
#      assert 'https://github.com/PortOfPortland/terraform-provider-activedirectory' in s
#      assert '0.5.1-pre' in s
