# terrascript/resource/cyrilgdn/vault.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:30:00 UTC)
import terrascript


class vault_ad_secret_backend(terrascript.Resource):
    pass


class vault_ad_secret_library(terrascript.Resource):
    pass


class vault_ad_secret_role(terrascript.Resource):
    pass


class vault_alicloud_auth_backend_role(terrascript.Resource):
    pass


class vault_approle_auth_backend_login(terrascript.Resource):
    pass


class vault_approle_auth_backend_role(terrascript.Resource):
    pass


class vault_approle_auth_backend_role_secret_id(terrascript.Resource):
    pass


class vault_audit(terrascript.Resource):
    pass


class vault_auth_backend(terrascript.Resource):
    pass


class vault_aws_auth_backend_cert(terrascript.Resource):
    pass


class vault_aws_auth_backend_client(terrascript.Resource):
    pass


class vault_aws_auth_backend_identity_whitelist(terrascript.Resource):
    pass


class vault_aws_auth_backend_login(terrascript.Resource):
    pass


class vault_aws_auth_backend_role(terrascript.Resource):
    pass


class vault_aws_auth_backend_role_tag(terrascript.Resource):
    pass


class vault_aws_auth_backend_roletag_blacklist(terrascript.Resource):
    pass


class vault_aws_auth_backend_sts_role(terrascript.Resource):
    pass


class vault_aws_secret_backend(terrascript.Resource):
    pass


class vault_aws_secret_backend_role(terrascript.Resource):
    pass


class vault_azure_auth_backend_config(terrascript.Resource):
    pass


class vault_azure_auth_backend_role(terrascript.Resource):
    pass


class vault_azure_secret_backend(terrascript.Resource):
    pass


class vault_azure_secret_backend_role(terrascript.Resource):
    pass


class vault_cert_auth_backend_role(terrascript.Resource):
    pass


class vault_consul_secret_backend(terrascript.Resource):
    pass


class vault_consul_secret_backend_role(terrascript.Resource):
    pass


class vault_database_secret_backend_connection(terrascript.Resource):
    pass


class vault_database_secret_backend_role(terrascript.Resource):
    pass


class vault_database_secret_backend_static_role(terrascript.Resource):
    pass


class vault_egp_policy(terrascript.Resource):
    pass


class vault_gcp_auth_backend(terrascript.Resource):
    pass


class vault_gcp_auth_backend_role(terrascript.Resource):
    pass


class vault_gcp_secret_backend(terrascript.Resource):
    pass


class vault_gcp_secret_roleset(terrascript.Resource):
    pass


class vault_gcp_secret_static_account(terrascript.Resource):
    pass


class vault_generic_endpoint(terrascript.Resource):
    pass


class vault_generic_secret(terrascript.Resource):
    pass


class vault_github_auth_backend(terrascript.Resource):
    pass


class vault_github_team(terrascript.Resource):
    pass


class vault_github_user(terrascript.Resource):
    pass


class vault_identity_entity(terrascript.Resource):
    pass


class vault_identity_entity_alias(terrascript.Resource):
    pass


class vault_identity_entity_policies(terrascript.Resource):
    pass


class vault_identity_group(terrascript.Resource):
    pass


class vault_identity_group_alias(terrascript.Resource):
    pass


class vault_identity_group_member_entity_ids(terrascript.Resource):
    pass


class vault_identity_group_policies(terrascript.Resource):
    pass


class vault_identity_oidc(terrascript.Resource):
    pass


class vault_identity_oidc_key(terrascript.Resource):
    pass


class vault_identity_oidc_key_allowed_client_id(terrascript.Resource):
    pass


class vault_identity_oidc_role(terrascript.Resource):
    pass


class vault_jwt_auth_backend(terrascript.Resource):
    pass


class vault_jwt_auth_backend_role(terrascript.Resource):
    pass


class vault_kubernetes_auth_backend_config(terrascript.Resource):
    pass


class vault_kubernetes_auth_backend_role(terrascript.Resource):
    pass


class vault_ldap_auth_backend(terrascript.Resource):
    pass


class vault_ldap_auth_backend_group(terrascript.Resource):
    pass


class vault_ldap_auth_backend_user(terrascript.Resource):
    pass


class vault_mfa_duo(terrascript.Resource):
    pass


class vault_mount(terrascript.Resource):
    pass


class vault_namespace(terrascript.Resource):
    pass


class vault_nomad_secret_backend(terrascript.Resource):
    pass


class vault_nomad_secret_role(terrascript.Resource):
    pass


class vault_okta_auth_backend(terrascript.Resource):
    pass


class vault_okta_auth_backend_group(terrascript.Resource):
    pass


class vault_okta_auth_backend_user(terrascript.Resource):
    pass


class vault_password_policy(terrascript.Resource):
    pass


class vault_pki_secret_backend(terrascript.Resource):
    pass


class vault_pki_secret_backend_cert(terrascript.Resource):
    pass


class vault_pki_secret_backend_config_ca(terrascript.Resource):
    pass


class vault_pki_secret_backend_config_urls(terrascript.Resource):
    pass


class vault_pki_secret_backend_crl_config(terrascript.Resource):
    pass


class vault_pki_secret_backend_intermediate_cert_request(terrascript.Resource):
    pass


class vault_pki_secret_backend_intermediate_set_signed(terrascript.Resource):
    pass


class vault_pki_secret_backend_role(terrascript.Resource):
    pass


class vault_pki_secret_backend_root_cert(terrascript.Resource):
    pass


class vault_pki_secret_backend_root_sign_intermediate(terrascript.Resource):
    pass


class vault_pki_secret_backend_sign(terrascript.Resource):
    pass


class vault_policy(terrascript.Resource):
    pass


class vault_quota_lease_count(terrascript.Resource):
    pass


class vault_quota_rate_limit(terrascript.Resource):
    pass


class vault_rabbitmq_secret_backend(terrascript.Resource):
    pass


class vault_rabbitmq_secret_backend_role(terrascript.Resource):
    pass


class vault_raft_snapshot_agent_config(terrascript.Resource):
    pass


class vault_rgp_policy(terrascript.Resource):
    pass


class vault_ssh_secret_backend_ca(terrascript.Resource):
    pass


class vault_ssh_secret_backend_role(terrascript.Resource):
    pass


class vault_terraform_cloud_secret_backend(terrascript.Resource):
    pass


class vault_terraform_cloud_secret_creds(terrascript.Resource):
    pass


class vault_terraform_cloud_secret_role(terrascript.Resource):
    pass


class vault_token(terrascript.Resource):
    pass


class vault_token_auth_backend_role(terrascript.Resource):
    pass


class vault_transform_alphabet(terrascript.Resource):
    pass


class vault_transform_role(terrascript.Resource):
    pass


class vault_transform_template(terrascript.Resource):
    pass


class vault_transform_transformation(terrascript.Resource):
    pass


class vault_transit_secret_backend_key(terrascript.Resource):
    pass


class vault_transit_secret_cache_config(terrascript.Resource):
    pass


__all__ = [
    "vault_ad_secret_backend",
    "vault_ad_secret_library",
    "vault_ad_secret_role",
    "vault_alicloud_auth_backend_role",
    "vault_approle_auth_backend_login",
    "vault_approle_auth_backend_role",
    "vault_approle_auth_backend_role_secret_id",
    "vault_audit",
    "vault_auth_backend",
    "vault_aws_auth_backend_cert",
    "vault_aws_auth_backend_client",
    "vault_aws_auth_backend_identity_whitelist",
    "vault_aws_auth_backend_login",
    "vault_aws_auth_backend_role",
    "vault_aws_auth_backend_role_tag",
    "vault_aws_auth_backend_roletag_blacklist",
    "vault_aws_auth_backend_sts_role",
    "vault_aws_secret_backend",
    "vault_aws_secret_backend_role",
    "vault_azure_auth_backend_config",
    "vault_azure_auth_backend_role",
    "vault_azure_secret_backend",
    "vault_azure_secret_backend_role",
    "vault_cert_auth_backend_role",
    "vault_consul_secret_backend",
    "vault_consul_secret_backend_role",
    "vault_database_secret_backend_connection",
    "vault_database_secret_backend_role",
    "vault_database_secret_backend_static_role",
    "vault_egp_policy",
    "vault_gcp_auth_backend",
    "vault_gcp_auth_backend_role",
    "vault_gcp_secret_backend",
    "vault_gcp_secret_roleset",
    "vault_gcp_secret_static_account",
    "vault_generic_endpoint",
    "vault_generic_secret",
    "vault_github_auth_backend",
    "vault_github_team",
    "vault_github_user",
    "vault_identity_entity",
    "vault_identity_entity_alias",
    "vault_identity_entity_policies",
    "vault_identity_group",
    "vault_identity_group_alias",
    "vault_identity_group_member_entity_ids",
    "vault_identity_group_policies",
    "vault_identity_oidc",
    "vault_identity_oidc_key",
    "vault_identity_oidc_key_allowed_client_id",
    "vault_identity_oidc_role",
    "vault_jwt_auth_backend",
    "vault_jwt_auth_backend_role",
    "vault_kubernetes_auth_backend_config",
    "vault_kubernetes_auth_backend_role",
    "vault_ldap_auth_backend",
    "vault_ldap_auth_backend_group",
    "vault_ldap_auth_backend_user",
    "vault_mfa_duo",
    "vault_mount",
    "vault_namespace",
    "vault_nomad_secret_backend",
    "vault_nomad_secret_role",
    "vault_okta_auth_backend",
    "vault_okta_auth_backend_group",
    "vault_okta_auth_backend_user",
    "vault_password_policy",
    "vault_pki_secret_backend",
    "vault_pki_secret_backend_cert",
    "vault_pki_secret_backend_config_ca",
    "vault_pki_secret_backend_config_urls",
    "vault_pki_secret_backend_crl_config",
    "vault_pki_secret_backend_intermediate_cert_request",
    "vault_pki_secret_backend_intermediate_set_signed",
    "vault_pki_secret_backend_role",
    "vault_pki_secret_backend_root_cert",
    "vault_pki_secret_backend_root_sign_intermediate",
    "vault_pki_secret_backend_sign",
    "vault_policy",
    "vault_quota_lease_count",
    "vault_quota_rate_limit",
    "vault_rabbitmq_secret_backend",
    "vault_rabbitmq_secret_backend_role",
    "vault_raft_snapshot_agent_config",
    "vault_rgp_policy",
    "vault_ssh_secret_backend_ca",
    "vault_ssh_secret_backend_role",
    "vault_terraform_cloud_secret_backend",
    "vault_terraform_cloud_secret_creds",
    "vault_terraform_cloud_secret_role",
    "vault_token",
    "vault_token_auth_backend_role",
    "vault_transform_alphabet",
    "vault_transform_role",
    "vault_transform_template",
    "vault_transform_transformation",
    "vault_transit_secret_backend_key",
    "vault_transit_secret_cache_config",
]