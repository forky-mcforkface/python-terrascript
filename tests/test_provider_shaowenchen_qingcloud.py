# tests/test_provider_shaowenchen_qingcloud.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:25:21 UTC)


def test_provider_import():
    import terrascript.provider.shaowenchen.qingcloud


def test_resource_import():
    from terrascript.resource.shaowenchen.qingcloud import qingcloud_eip

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_instance

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_keypair

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_loadbalancer

    from terrascript.resource.shaowenchen.qingcloud import (
        qingcloud_loadbalancer_backend,
    )

    from terrascript.resource.shaowenchen.qingcloud import (
        qingcloud_loadbalancer_listener,
    )

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_security_group

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_security_group_rule

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_server_certificate

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_tag

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_volume

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_vpc

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_vpc_static

    from terrascript.resource.shaowenchen.qingcloud import qingcloud_vxnet


def test_datasource_import():
    from terrascript.data.shaowenchen.qingcloud import qingcloud_vpn_cert


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.shaowenchen.qingcloud
#
#      t = terrascript.provider.shaowenchen.qingcloud.qingcloud()
#      s = str(t)
#
#      assert 'https://github.com/shaowenchen/terraform-provider-qingcloud' in s
#      assert '1.2.6' in s