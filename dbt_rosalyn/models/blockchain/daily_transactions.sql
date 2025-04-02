
/*
    Aggregate daily transactions across chains.
*/

{{ config(
    materialized='table',
    post_hook=[
        """
        EXPORT DATA
            OPTIONS (
                uri = 'gs://blockchain_proto/daily_transactions_*.csv',
                format = 'csv',
                overwrite = true,
                header = true,
                field_delimiter = ',')
        AS (
            SELECT date, transactions, blockchain
            FROM {{ this }}
            ORDER BY date
        );
        """
    ]
) }}

with ethereum as (
    select 
        date,
        tx_count as transactions,
        'ethereum' as blockchain
    from `prototype-451312.Raw.ethereum_daily_transactions`
),
base as (
    select 
        date,
        tx_count as transactions,
        'base' as blockchain
    from `prototype-451312.Raw.base_daily_transactions`
),
optimism as (
    select 
        date,
        tx_count as transactions,
        'optimism' as blockchain
    from `prototype-451312.Raw.optimism_daily_transactions`
),
arbitrum as (
    select 
        date,
        tx_count as transactions,
        'arbitrum' as blockchain
    from `prototype-451312.Raw.arbitrum_daily_transactions`
),
polygon as (
    select 
        date,
        tx_count as transactions,
        'polygon' as blockchain
    from `prototype-451312.Raw.polygon_daily_transactions`
)
{{ union_date(['ethereum', 'base', 'optimism', 'arbitrum', 'polygon'], ascending=true) }}