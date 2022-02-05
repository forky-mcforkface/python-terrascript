# tests/test_provider_ukfast_ecloud.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:15:38 UTC)


def test_provider_import():
    import terrascript.provider.ukfast.ecloud


def test_resource_import():
    from terrascript.resource.ukfast.ecloud import ecloud_firewallpolicy

    from terrascript.resource.ukfast.ecloud import ecloud_firewallrule

    from terrascript.resource.ukfast.ecloud import ecloud_floatingip

    from terrascript.resource.ukfast.ecloud import ecloud_host

    from terrascript.resource.ukfast.ecloud import ecloud_hostgroup

    from terrascript.resource.ukfast.ecloud import ecloud_instance

    from terrascript.resource.ukfast.ecloud import ecloud_network

    from terrascript.resource.ukfast.ecloud import ecloud_networkpolicy

    from terrascript.resource.ukfast.ecloud import ecloud_networkrule

    from terrascript.resource.ukfast.ecloud import ecloud_router

    from terrascript.resource.ukfast.ecloud import ecloud_ssh_keypair

    from terrascript.resource.ukfast.ecloud import ecloud_volume

    from terrascript.resource.ukfast.ecloud import ecloud_vpc

    from terrascript.resource.ukfast.ecloud import ecloud_vpn_endpoint

    from terrascript.resource.ukfast.ecloud import ecloud_vpn_service

    from terrascript.resource.ukfast.ecloud import ecloud_vpn_session


def test_datasource_import():
    from terrascript.data.ukfast.ecloud import ecloud_availability_zone

    from terrascript.data.ukfast.ecloud import ecloud_firewallpolicy

    from terrascript.data.ukfast.ecloud import ecloud_firewallrule

    from terrascript.data.ukfast.ecloud import ecloud_floatingip

    from terrascript.data.ukfast.ecloud import ecloud_host

    from terrascript.data.ukfast.ecloud import ecloud_hostgroup

    from terrascript.data.ukfast.ecloud import ecloud_hostspec

    from terrascript.data.ukfast.ecloud import ecloud_image

    from terrascript.data.ukfast.ecloud import ecloud_instance

    from terrascript.data.ukfast.ecloud import ecloud_network

    from terrascript.data.ukfast.ecloud import ecloud_networkpolicy

    from terrascript.data.ukfast.ecloud import ecloud_networkrule

    from terrascript.data.ukfast.ecloud import ecloud_nic

    from terrascript.data.ukfast.ecloud import ecloud_region

    from terrascript.data.ukfast.ecloud import ecloud_router

    from terrascript.data.ukfast.ecloud import ecloud_router_throughput

    from terrascript.data.ukfast.ecloud import ecloud_ssh_keypair

    from terrascript.data.ukfast.ecloud import ecloud_volume

    from terrascript.data.ukfast.ecloud import ecloud_vpc

    from terrascript.data.ukfast.ecloud import ecloud_vpn_endpoint

    from terrascript.data.ukfast.ecloud import ecloud_vpn_profile_group

    from terrascript.data.ukfast.ecloud import ecloud_vpn_service

    from terrascript.data.ukfast.ecloud import ecloud_vpn_session


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.ukfast.ecloud
#
#      t = terrascript.provider.ukfast.ecloud.ecloud()
#      s = str(t)
#
#      assert 'https://github.com/ukfast/terraform-provider-ecloud' in s
#      assert '2.0.0' in s