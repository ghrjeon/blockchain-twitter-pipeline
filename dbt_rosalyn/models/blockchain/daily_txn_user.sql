/*
    Calculate daily transactions per user across chains.
*/

{{ config(
    materialized='table',
    post_hook=[
        """
        EXPORT DATA
            OPTIONS (
                uri = 'gs://blockchain_proto/daily_txn_user_*.csv',
                format = 'csv',
                overwrite = true,
                header = true,
                field_delimiter = ',')
        AS (
            SELECT date, txn_per_user, blockchain
            FROM {{ this }}
            ORDER BY date
        );
        """
    ]
) }}

with transactions as (
    select * from `prototype-451312.Stage.daily_transactions`
),
users as (
    select * from `prototype-451312.Stage.daily_users`
),
combined_data as (
    select 
        transactions.date,
        transactions.transactions,
        users.users,
        transactions.blockchain
    from transactions
    left join users on transactions.date = users.date and transactions.blockchain = users.blockchain
)
select 
    date,
    (transactions/users) as txn_per_user,
    blockchain
from combined_data
order by date