/**
 * mod_serverheader for Apache HTTPD 2.4
 * Copyright (c) 2017 Robert Bost <bostrt at gmail dot com>
 * 
 * All Rights Reserved
 * You may use, distribute and modify this code under the
 * terms of the Apache License Version 2.0.
 * 
 * You should have received a copy of the Apache LcieseXYZApache License Version
 * 2.0 license with this file. If not, please write to: 
 * bostrt at gmail dot com, or visit: 
 * http://www.apache.org/licenses/LICENSE-2.0.html
 */

#include <httpd.h>
#include <http_config.h>
#include <http_log.h>

module AP_MODULE_DECLARE_DATA server_header_module;

typedef struct {
  const char *new_server_header;
} server_header_config;

static const char * server_header(cmd_parms *cmd, void *xxx, const char *arg)
{
    const char *err = ap_check_cmd_context(cmd, GLOBAL_ONLY);
    if (err != NULL) {
      return err;
    }

    server_header_config *config = ap_get_module_config(cmd->server->module_config, &server_header_module);
    config->new_server_header = arg;
    return NULL;
}

static int hook_post_config(apr_pool_t *p, apr_pool_t *plog, apr_pool_t *ptemp, server_rec *s)
{
  char * banner = ap_get_server_banner();
  int banner_len = strlen(banner);
  server_header_config *config = ap_get_module_config(s->module_config, &server_header_module);
  int new_banner_len;

  if (config->new_server_header == NULL) {
    ap_log_error(APLOG_MARK, APLOG_INFO, 0, s, "No custom server header or banner configured.");
    return DECLINED;
  }
  
  new_banner_len = strlen(config->new_server_header);
  
  // Make sure banner is long enough to store our new contents.
  if (banner_len < new_banner_len) {
    ap_log_error(APLOG_MARK, APLOG_CRIT, 0, s, "ServerHeader directive (\"%s\") is too long. Please set ServerTokens to Full or limit your ServerHeader length to %d. [old: %d, new: %d]", config->new_server_header, banner_len, new_banner_len);
    return DONE;
  } else {
    strcpy(banner, config->new_server_header);
    ap_log_error(APLOG_MARK, APLOG_NOTICE, 0, s, "Setting server header and banner to %s", banner);
  }
  return OK;
}

static const command_rec commands[] =
{
  AP_INIT_TAKE1("ServerHeader", server_header, NULL, RSRC_CONF,
                "Modify Server header contents"),
  { NULL }
};

static void register_hooks(apr_pool_t *p)
{
  ap_hook_post_config(hook_post_config, NULL, NULL, APR_HOOK_REALLY_LAST);
}

AP_DECLARE_MODULE( serverheader ) =
{
  STANDARD20_MODULE_STUFF,
  NULL,
  NULL,
  NULL,
  NULL,
  commands,
  register_hooks,
};
