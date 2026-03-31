CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_pattern TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT first_name, phone_number FROM phonebook
    WHERE first_name ILIKE '%' || p_pattern || '%'
       OR phone_number ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;