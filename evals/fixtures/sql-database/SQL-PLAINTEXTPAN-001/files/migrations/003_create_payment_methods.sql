CREATE TABLE payment_methods (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    customer_id BIGINT NOT NULL,
    -- Vulnerable: the full card number (PAN) and CVV are stored in plain,
    -- unencrypted columns. Anyone with read access to this table - a
    -- support engineer, a compromised reporting service, a SQL-injection
    -- finding anywhere else in the codebase, or a stolen backup - gets the
    -- complete card number and CVV directly, not a tokenized or truncated
    -- reference. This also fails PCI-DSS storage requirements outright,
    -- which prohibit storing CVV after authorization and require the PAN
    -- to be encrypted or replaced with a token at rest.
    card_number VARCHAR(19) NOT NULL,
    cvv VARCHAR(4) NOT NULL,
    expiry_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
