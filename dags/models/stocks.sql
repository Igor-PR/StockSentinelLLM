with brazilian_stocks as (
    select * from {{ ref('stg_br_stocks') }}
),
us_stocks as (
    select * from {{ ref('stg_us_stocks') }}
)
select * from brazilian_stocks
union all
select * from us_stocks
