<?php

add_action('rest_api_init', function () {
    register_rest_route('shop/v1', '/customers/(?P<id>\d+)', [
        'methods' => 'GET',
        'callback' => 'shop_get_customer',
        // Vulnerable: permission_callback is hardcoded to '__return_true',
        // which tells WordPress this endpoint requires no authentication or
        // capability check at all. /wp-json/shop/v1/customers/<id> - which
        // returns the customer's name, address, and order history - is
        // reachable by anyone on the internet for any customer id, logged
        // in or not.
        'permission_callback' => '__return_true',
    ]);
});

function shop_get_customer($request)
{
    global $wpdb;
    $customer = $wpdb->get_row(
        $wpdb->prepare("SELECT name, address, phone FROM {$wpdb->prefix}shop_customers WHERE id = %d", $request['id'])
    );
    return rest_ensure_response($customer);
}
