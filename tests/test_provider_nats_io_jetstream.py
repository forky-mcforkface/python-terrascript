# tests/test_provider_nats-io_jetstream.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:19:35 UTC)


def test_provider_import():
    import terrascript.provider.nats_io.jetstream


def test_resource_import():
    from terrascript.resource.nats_io.jetstream import jetstream_consumer

    from terrascript.resource.nats_io.jetstream import jetstream_kv_bucket

    from terrascript.resource.nats_io.jetstream import jetstream_stream

    from terrascript.resource.nats_io.jetstream import jetstream_stream_template


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.nats_io.jetstream
#
#      t = terrascript.provider.nats_io.jetstream.jetstream()
#      s = str(t)
#
#      assert 'https://github.com/nats-io/terraform-provider-jetstream' in s
#      assert '0.0.26' in s
