<?php
define('DB_NAME', 'wordpress');
define('DB_USER', 'wp_user');
define('DB_PASSWORD', getenv('WORDPRESS_DB_PASSWORD'));
define('DB_HOST', 'localhost');

// Vulnerable: WP_DEBUG and WP_DEBUG_DISPLAY are both enabled on what this
// file's own deployment comment below identifies as the production config.
// Every unhandled PHP notice, warning, or fatal error is rendered directly
// in the page response - including file paths, plugin/theme internals, and
// occasionally query fragments - to any visitor who triggers one.
define('WP_DEBUG', true);
define('WP_DEBUG_DISPLAY', true);
define('WP_DEBUG_LOG', false);

// Deployment target: production (wordpress.example.com)

require_once ABSPATH . 'wp-settings.php';
