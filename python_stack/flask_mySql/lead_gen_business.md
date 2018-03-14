# Lead Gen Business

1. What query would you run to get the total revenue for March of 2012?

    ```sql
    SELECT MONTHNAME(charged_datetime) as month, SUM(amount) as revenue FROM billing
    WHERE YEAR(charged_datetime) = 2012 && MONTH(charged_datetime) = 3;
    ```

2. What query would you run to get total revenue collected from the client with an id of 2?

    ```sql
    SELECT client_id, SUM(amount) as total_revenue FROM billing
    WHERE client_id = 2;
    ```

3. What query would you run to get all the sites that client=10 owns?

    ```sql
    SELECT domain_name as website, client_id FROM sites
    WHERE client_id = 10;
    ```

4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?

    ```sql
    SELECT client_id, COUNT(domain_name) as number_of_websites, MONTHNAME(created_datetime) as month_created, YEAR(created_datetime) as year_created FROM sites
    WHERE client_id = 1
    GROUP BY month_created, year_created
    ORDER BY year_created, month_created;
    ```

5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?

    ```sql
    SELECT sites.domain_name as website, COUNT(leads.leads_id) as number_of_leads, DATE_FORMAT(sites.created_datetime, "%M %e, %Y") AS date_generated  FROM leads
    JOIN sites ON leads.site_id = sites.site_id
    WHERE sites.created_datetime >= "2011/01/01" AND sites.created_datetime <= "2011/02/15"
    GROUP BY sites.domain_name;
    ```

6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?

    ```sql
    SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) as client_name, COUNT(leads.leads_id) as number_of_leads  FROM clients
    JOIN sites ON sites.client_id = clients.client_id
    JOIN leads ON leads.site_id = sites.site_id
    WHERE YEAR(leads.registered_datetime) = 2011
    GROUP BY clients.client_id
    ```

7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?

    ```sql
    SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) as client_name, COUNT(clients.client_id) as number_of_leads, MONTHNAME(leads.registered_datetime) AS month_generated FROM clients
    JOIN sites ON sites.client_id = clients.client_id
    JOIN leads ON leads.site_id = sites.site_id
    WHERE YEAR(leads.registered_datetime) = 2011 && MONTH(leads.registered_datetime) < 7
    GROUP BY leads.registered_datetime, clients.client_id
    ORDER BY leads.registered_datetime, clients.client_id;
    ```

8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.

    ```sql
    SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, sites.domain_name as website, COUNT(sites.domain_name) as number_of_leads FROM clients
    JOIN sites ON sites.client_id = clients.client_id
    JOIN leads ON leads.site_id = sites.site_id
    GROUP BY sites.domain_name, clients.first_name, client_name, clients.client_id
    ORDER BY clients.client_id, number_of_leads DESC;
    ```

    ```sql
    SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) as client_name, sites.domain_name as website, COUNT(sites.site_id) AS number_of_leads FROM clients
    JOIN sites ON sites.client_id = clients.client_id
    JOIN leads ON leads.site_id = sites.site_id
    GROUP BY sites.site_id
    ORDER BY clients.client_id, number_of_leads DESC;
    ```

9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.

    ```sql
    SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, SUM(billing.amount) as Total_Revenue, MONTHNAME(billing.charged_datetime) as month_charge, YEAR(billing.charged_datetime) as year_charge FROM clients
    JOIN billing ON clients.client_id = billing.client_id
    GROUP BY month_charge, year_charge, client_name, clients.client_id, billing.amount
    ORDER BY clients.client_id, month_charge, year_charge;
    ```

10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)

    ```sql
    SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, GROUP_CONCAT(" ", sites.domain_name) AS sites FROM clients
    JOIN sites ON sites.client_id
    GROUP BY clients.client_id
    ```