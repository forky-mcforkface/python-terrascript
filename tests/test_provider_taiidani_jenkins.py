# tests/test_provider_taiidani_jenkins.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:19:30 UTC)


def test_provider_import():
    import terrascript.provider.taiidani.jenkins


def test_resource_import():
    from terrascript.resource.taiidani.jenkins import jenkins_credential_secret_file

    from terrascript.resource.taiidani.jenkins import jenkins_credential_secret_text

    from terrascript.resource.taiidani.jenkins import jenkins_credential_ssh

    from terrascript.resource.taiidani.jenkins import jenkins_credential_username

    from terrascript.resource.taiidani.jenkins import jenkins_credential_vault_approle

    from terrascript.resource.taiidani.jenkins import jenkins_folder

    from terrascript.resource.taiidani.jenkins import jenkins_job


def test_datasource_import():
    from terrascript.data.taiidani.jenkins import jenkins_credential_username

    from terrascript.data.taiidani.jenkins import jenkins_credential_vault_approle

    from terrascript.data.taiidani.jenkins import jenkins_folder

    from terrascript.data.taiidani.jenkins import jenkins_job


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.taiidani.jenkins
#
#      t = terrascript.provider.taiidani.jenkins.jenkins()
#      s = str(t)
#
#      assert 'https://github.com/taiidani/terraform-provider-jenkins' in s
#      assert '0.9.0' in s
