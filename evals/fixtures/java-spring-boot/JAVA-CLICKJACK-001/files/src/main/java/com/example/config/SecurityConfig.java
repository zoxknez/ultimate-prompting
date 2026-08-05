package com.example.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        // Vulnerable: frame options protection is explicitly disabled, and no
        // Content-Security-Policy frame-ancestors directive is set anywhere
        // else in this project. Every authenticated page, including the
        // account settings and funds-transfer forms, can be embedded in an
        // invisible iframe on an attacker's site and clickjacked into
        // performing actions the user never intended.
        http.headers(headers -> headers.frameOptions(frame -> frame.disable()));

        return http.build();
    }
}
