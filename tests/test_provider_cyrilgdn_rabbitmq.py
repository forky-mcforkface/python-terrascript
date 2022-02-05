# tests/test_provider_cyrilgdn_rabbitmq.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:25:26 UTC)


def test_provider_import():
    import terrascript.provider.cyrilgdn.rabbitmq


def test_resource_import():
    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_binding

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_exchange

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_federation_upstream

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_permissions

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_policy

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_queue

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_shovel

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_topic_permissions

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_user

    from terrascript.resource.cyrilgdn.rabbitmq import rabbitmq_vhost


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.cyrilgdn.rabbitmq
#
#      t = terrascript.provider.cyrilgdn.rabbitmq.rabbitmq()
#      s = str(t)
#
#      assert 'https://github.com/cyrilgdn/terraform-provider-rabbitmq' in s
#      assert '1.6.0' in s