/*
    Aggregate daily users across chains.
*/

{{ config(
    materialized='table',
    post_hook=[
        """
        EXPORT DATA
            OPTIONS (
                uri = 'gs://blockchain_proto/daily_users_*.csv',
                format = 'csv',
                overwrite = true,
                header = true,
                field_delimiter = ',')
        AS (
            SELECT date, users, blockchain
            FROM {{ this }}
            ORDER BY date
        );
        """
    ]
) }}

with ethereum as (
    select 
        date,
        user_count as users,
        'ethereum' as blockchain
    from `prototype-451312.Raw.ethereum_daily_users`
),
base as (
    select 
        date,
        user_count as users,
        'base' as blockchain
    from `prototype-451312.Raw.base_daily_users`
),
optimism as (
    select 
        date,
        user_count as users,
        'optimism' as blockchain
    from `prototype-451312.Raw.optimism_daily_users`
),
arbitrum as (
    select 
        date,
        user_count as users,
        'arbitrum' as blockchain
    from `prototype-451312.Raw.arbitrum_daily_users`
)

{{ union_date(['ethereum', 'base', 'optimism', 'arbitrum'], ascending=true) }}