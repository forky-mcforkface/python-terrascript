# tests/test_provider_oktadeveloper_oktaasa.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:23:27 UTC)


def test_provider_import():
    import terrascript.provider.oktadeveloper.oktaasa


def test_resource_import():
    from terrascript.resource.oktadeveloper.oktaasa import oktaasa_assign_group

    from terrascript.resource.oktadeveloper.oktaasa import oktaasa_create_group

    from terrascript.resource.oktadeveloper.oktaasa import oktaasa_enrollment_token

    from terrascript.resource.oktadeveloper.oktaasa import oktaasa_project


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.oktadeveloper.oktaasa
#
#      t = terrascript.provider.oktadeveloper.oktaasa.oktaasa()
#      s = str(t)
#
#      assert 'https://github.com/oktadeveloper/terraform-provider-oktaasa' in s
#      assert '1.0.1' in s