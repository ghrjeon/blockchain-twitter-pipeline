/*
    Aggregate daily twitter keywords across chains.
*/

{{ config(
    materialized='table',
    post_hook=[
        """
        EXPORT DATA
            OPTIONS (
                uri = 'gs://blockchain_proto/daily_keywords_*.csv',
                format = 'csv',
                overwrite = true,
                header = true,
                field_delimiter = ';')
        AS (
            SELECT date, keywords, ecosystem
            FROM {{ this }}
            ORDER BY date desc
        );
        """
    ]
) }}


with ethereum as (
    select 
        date,
        keywords as keywords,
        'ethereum' as ecosystem
    from `prototype-451312.Raw.ethereum_keywords`
),
solana as (
    select 
        date,
        keywords as keywords,
        'solana' as ecosystem
    from `prototype-451312.Raw.solana_keywords`
),
bitcoin as (
    select 
        date,
        keywords as keywords,
        'bitcoin' as ecosystem
    from `prototype-451312.Raw.bitcoin_keywords`
),
nft as (
    select 
        date,
        keywords as keywords,
        'nft' as blockchain
    from `prototype-451312.Raw.nft_keywords`
),
depin as (
    select 
        date,
        keywords as keywords,
        'depin' as ecosystem
    from `prototype-451312.Raw.depin_keywords`
),
defi as (
    select 
        date,
        keywords as keywords,
        'defi' as ecosystem
    from `prototype-451312.Raw.defi_keywords`
)



{{ union_date(['ethereum', 'solana', 'bitcoin', 'nft', 'depin', 'defi'], ascending=false) }}