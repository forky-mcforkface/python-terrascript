# terrascript/vault/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class vault_approle_auth_backend_role_id(terrascript.Data):
    pass


class vault_auth_backend(terrascript.Data):
    pass


class vault_aws_access_credentials(terrascript.Data):
    pass


class vault_azure_access_credentials(terrascript.Data):
    pass


class vault_generic_secret(terrascript.Data):
    pass


class vault_identity_entity(terrascript.Data):
    pass


class vault_identity_group(terrascript.Data):
    pass


class vault_kubernetes_auth_backend_config(terrascript.Data):
    pass


class vault_kubernetes_auth_backend_role(terrascript.Data):
    pass


class vault_policy_document(terrascript.Data):
    pass
