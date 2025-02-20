/*
    Aggregate daily twitter keywords across chains.
*/

{{ config(
    materialized='table',
    post_hook=[
        """
        EXPORT DATA
            OPTIONS (
                uri = 'gs://blockchain_proto/top_tweets_*.csv',
                format = 'csv',
                overwrite = true,
                header = true,
                field_delimiter = ';')
        AS (
            SELECT date, id, text, user_screen_name, favorite_count, bookmark_count, retweet_count, ecosystem
            FROM {{ this }}
            ORDER BY date desc
        );
        """
    ]
) }}


with ethereum as (
    select 
        date,
        id, 
        text,
        user_screen_name,
        favorite_count,
        bookmark_count,
        retweet_count,
        'ethereum' as ecosystem
    from `prototype-451312.Raw.ethereum_tweets`
),
solana as (
    select 
        date,
        id, 
        text,
        user_screen_name,
        favorite_count,
        bookmark_count,
        retweet_count,
        'solana' as ecosystem
    from `prototype-451312.Raw.solana_tweets`
),
bitcoin as (
    select 
        date,
        id, 
        text,
        user_screen_name,
        favorite_count,
        bookmark_count,
        retweet_count,
        'bitcoin' as ecosystem
    from `prototype-451312.Raw.bitcoin_tweets`
),
nft as (
    select 
        date,
        id, 
        text,
        user_screen_name,
        favorite_count,
        bookmark_count,
        retweet_count,
        'nft' as ecosystem
    from `prototype-451312.Raw.nft_tweets`
),
depin as (
    select 
        date,
        id, 
        text,
        user_screen_name,
        favorite_count,
        bookmark_count,
        retweet_count,
        'depin' as ecosystem
    from `prototype-451312.Raw.depin_tweets`
),
defi as (
    select 
        date,
        id, 
        text,
        user_screen_name,
        favorite_count,
        bookmark_count,
        retweet_count,
        'defi' as ecosystem
    from `prototype-451312.Raw.defi_tweets`
),
aggregate as (
{{ union_date(['ethereum', 'solana', 'bitcoin', 'nft', 'depin', 'defi'], ascending=false) }}
),
ranked as (
select *
from (
    select 
        date,
        CAST(id AS STRING) as id, 
        text,
        user_screen_name,
        favorite_count,
        bookmark_count,
        retweet_count,
        ecosystem,
        rank() over (partition by ecosystem, date order by bookmark_count desc) as rank
    from aggregate
    where date >= current_date() - interval 7 day
) 
where rank <= 5
)
select * from ranked    



