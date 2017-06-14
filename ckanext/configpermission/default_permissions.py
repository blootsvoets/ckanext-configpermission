from ckanext.configpermission import default_roles

default_permissions = [{'display_name': 'Create Group', 'name': 'group_create', 'role': default_roles.SYSADMIN},
                       {'display_name': 'Show Package', 'name': 'package_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'current_package_list_with_resources', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'related_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'file_upload', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_list_authz', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'related_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'revision_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_member_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'member_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_revision_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'site_read', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_member_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_followee_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'vocabulary_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'request_reset', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'related_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_autocomplete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'get_package_object', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_revision_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_create_default_resource_views', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'related_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_invite', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_change_state', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_followee_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'dataset_followee_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'member_roles_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'revision_change_state', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'revision_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'logic_auth', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'dataset_purge', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_autocomplete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_revision_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_patch', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'revision_undelete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_view_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'dashboard_new_activities_count', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_show_rest', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_status_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_patch', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'config_option_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_autocomplete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_change_state', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_view_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'vocabulary_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_purge', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'tag_show_rest', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_follower_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_followee_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'term_translation_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'format_autocomplete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'tag_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_list_available', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_view_clear', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_relationship_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'revision_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'dashboard_mark_activities_old', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_update_rest', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'vocabulary_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'config_option_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'get_group_object', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_purge', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_resource_reorder', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'bulk_update_public', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'logic', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'tag_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_follower_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'config_option_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'vocabulary_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_relationships_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_create_default_resource_views', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_patch', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'tag_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'dataset_follower_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'tag_autocomplete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_view_reorder', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'get_site_user', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'task_status_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_reset', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'send_email_notifications', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'vocabulary_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'license_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'task_status_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'bulk_update_private', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'rating_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_list_for_user', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'member_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_relationship_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_member_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_view_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_generate_apikey', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_edit_permissions', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_search', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'tag_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'sysadmin', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_owner_org_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_relationship_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_view_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'bulk_update_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'get_related_object', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_create_rest', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_patch', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'get_resource_object', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_member_delete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_show_rest', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'dashboard_activity_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_view_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'help_show', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'resource_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_autocomplete', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_follower_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'group_create_rest', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'task_status_update', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'followee_list', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'activity_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'package_update_rest', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'organization_create', 'role': default_roles.SYSADMIN},
                       # {'display_name': 'test', 'name': 'user_list', 'role': default_roles.SYSADMIN},
                       ]