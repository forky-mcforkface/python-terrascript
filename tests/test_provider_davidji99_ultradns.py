# tests/test_provider_davidji99_ultradns.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:29:41 UTC)


def test_provider_import():
    import terrascript.provider.davidji99.ultradns


def test_resource_import():
    from terrascript.resource.davidji99.ultradns import ultradns_dirpool

    from terrascript.resource.davidji99.ultradns import ultradns_probe_http

    from terrascript.resource.davidji99.ultradns import ultradns_probe_ping

    from terrascript.resource.davidji99.ultradns import ultradns_rdpool

    from terrascript.resource.davidji99.ultradns import ultradns_record

    from terrascript.resource.davidji99.ultradns import ultradns_tcpool


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.davidji99.ultradns
#
#      t = terrascript.provider.davidji99.ultradns.ultradns()
#      s = str(t)
#
#      assert 'https://github.com/davidji99/terraform-provider-ultradns' in s
#      assert '2.1.0' in s