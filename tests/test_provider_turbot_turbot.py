# tests/test_provider_turbot_turbot.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:29:24 UTC)


def test_provider_import():
    import terrascript.provider.turbot.turbot


def test_resource_import():
    from terrascript.resource.turbot.turbot import turbot_file

    from terrascript.resource.turbot.turbot import turbot_folder

    from terrascript.resource.turbot.turbot import turbot_google_directory

    from terrascript.resource.turbot.turbot import turbot_grant

    from terrascript.resource.turbot.turbot import turbot_grant_activation

    from terrascript.resource.turbot.turbot import turbot_ldap_directory

    from terrascript.resource.turbot.turbot import turbot_local_directory

    from terrascript.resource.turbot.turbot import turbot_local_directory_user

    from terrascript.resource.turbot.turbot import turbot_mod

    from terrascript.resource.turbot.turbot import turbot_policy_setting

    from terrascript.resource.turbot.turbot import turbot_profile

    from terrascript.resource.turbot.turbot import turbot_resource

    from terrascript.resource.turbot.turbot import turbot_saml_directory

    from terrascript.resource.turbot.turbot import turbot_shadow_resource

    from terrascript.resource.turbot.turbot import turbot_smart_folder

    from terrascript.resource.turbot.turbot import turbot_smart_folder_attachment

    from terrascript.resource.turbot.turbot import turbot_turbot_directory


def test_datasource_import():
    from terrascript.data.turbot.turbot import turbot_control

    from terrascript.data.turbot.turbot import turbot_policy_value

    from terrascript.data.turbot.turbot import turbot_resource


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.turbot.turbot
#
#      t = terrascript.provider.turbot.turbot.turbot()
#      s = str(t)
#
#      assert 'https://github.com/turbot/terraform-provider-turbot' in s
#      assert '1.8.2' in s